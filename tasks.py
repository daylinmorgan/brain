#!/usr/bin/env python3

if not (
    (_i := __import__)("importlib.util").util.find_spec("swydd")
    or (_src := _i("pathlib").Path(__file__).parent / "swydd/__init__.py").is_file()
):  # noqa # https://github.com/daylinmorgan/swydd?tab=readme-ov-file#automagic-snippet
    _r = _i("urllib.request").request.urlopen("https://swydd.dayl.in/swydd.py")
    _src.parent.mkdir(exist_ok=True)
    _src.write_text(_r.read().decode())

from pathlib import Path
from swydd import task, sub, cli, setenv, get

setenv(
    "HUGO_MODULE_REPLACEMENTS",
    "github.com/daylinmorgan/brain-stem -> brain-stem",
)


@task
def add_words():
    """add 'misspelled' words to project-words.txt"""
    dictionary = Path(__file__).parent / "project-words.txt"
    new_words = get("cspell lint slipbox --words-only").strip().splitlines()
    words = dictionary.read_text().splitlines()
    dictionary.write_text("\n".join(sorted((*words, *new_words))))


@task
def spell_check():
    """find all misspelled words w/cspell"""
    sub("cspell lint slipbox")


@task
def think():
    """commit the slipbox with :brain: commit"""
    # sub("git commit -m ':brain:' -- slipbox")
    sub("jj ci -m ':brain:' -- slipbox")


@task
def serve():
    """run hugo server"""
    sub("hugo server -s hugo --disableFastRender")


@task
def build():
    """build hugo server"""
    sub("hugo -s hugo")


cli("serve")
