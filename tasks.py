#!/usr/bin/env python3

# https://github.com/daylinmorgan/charman (readme path to automagic fetch)
# fmt: off
if not (src := __import__("pathlib").Path(__file__).parent / "swydd/__init__.py").is_file(): # noqa
    try: __import__("swydd") # noqa
    except ImportError:
        import sys; from urllib.request import urlopen; from urllib.error import URLError # noqa
        try: r = urlopen("https://raw.githubusercontent.com/daylinmorgan/swydd/main/src/swydd/__init__.py") # noqa
        except URLError as e: sys.exit(f"{e}\n") # noqa
        src.parent.mkdir(exist_ok=True); src.write_text(r.read().decode("utf-8")); # noqa
# fmt: on

import swydd as s


s.define_env("HUGO_MODULE_REPLACEMENTS","github.com/daylinmorgan/brain-stem -> brain-stem")

@s.task
def think():
    """commit the slipbox with :brain: commit"""
    s.sh("git commit -m ':brain:' -- slipbox")

@s.task
def serve():
    """run hugo server"""
    s.sh("hugo server -s hugo")


@s.task
def build():
    """build hugo server"""
    s.sh("hugo -s hugo")


s.cli()

