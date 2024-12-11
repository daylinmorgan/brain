#!/usr/bin/env python3

if not (
    (_i := __import__)("importlib.util").util.find_spec("swydd")
    or (_src := _i("pathlib").Path(__file__).parent / "swydd/__init__.py").is_file()
):  # noqa # https://github.com/daylinmorgan/swydd?tab=readme-ov-file#automagic-snippet
    _r = _i("urllib.request").request.urlopen("https://swydd.dayl.in/swydd.py")
    _src.parent.mkdir(exist_ok=True)
    _src.write_text(_r.read().decode())

from pathlib import Path
import subprocess
import sys
from swydd import task, sub, cli, setenv

setenv(
    "HUGO_MODULE_REPLACEMENTS",
    "github.com/daylinmorgan/brain-stem -> brain-stem",
)


@task
def spell_check():
    """find all misspelled words and print to stdout"""
    text = ""
    for f in (Path(__file__).parent / "slipbox").iterdir():
        text += f.read_text()
    # TODO: add support for this in swydd?
    output = subprocess.run(
        ["aspell", "--conf=./.aspell/aspell.conf", "list"],
        input=text,
        text=True,
        capture_output=True,
    )
    if output.returncode != 0:
        sys.exit("error running aspell")

    print("\n".join(sorted(set(output.stdout.splitlines()))))


@task
def spell_review():
    """run spell check on files using aspell"""
    for f in (Path(__file__).parent / "slipbox").iterdir():
        sub(f"aspell --conf=./.aspell/aspell.conf check {f}")


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
