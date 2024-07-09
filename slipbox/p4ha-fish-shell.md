---
title: Fish Shell
tags:
  - shell
---

Fish doesn't have process substitution like is found in bash and [zsh](v6l4-zshell.md).

It does have process substitution but it works differently, see `psub --help`,
for more info and below for a basic example.

ZSH:
```zsh
python3 <(curl -fsSL viv.dayl.in/viv.py)
```

FISH:
```fish
python3 (curl -fsSL viv.dayl.in/viv.py | psub)
```

The builtin [`fish_add_path`](https://fishshell.com/docs/current/cmds/fish_add_path.html)
has a feature that I was previously accomplishing using zsh wildcards

Namely to add paths to `$PATH` only if the exist for example the below with both prepend paths to $PATH only if the exist.

ZSH:

```zsh
path=(
  $HOME/.{go,cargo,pyenv,pixi}/bin(N)

  /opt/local/{,s}bin(N)
  /usr/{,local/}{,s}bin(N)

  $path
)
```

FISH:

```fish
fish_add_path /opt/local/{,s}bin
fish_add_path /usr/{,local}/{,s}bin
fish_add_path $HOME/.{go,cargo,pyenv,pixi,zig}/bin
```

My fish experiment lasted less than a day. I'll probably return to fish someday in the future.
Though who knows maybe `nushell` will actually make a case as an interactive shell.
When attempting to install it on a remote server resulted in a broken binary that couldn't produce help output.

Once this [PR](https://github.com/fish-shell/fish-shell/pull/10367) is fleshed out I'll probably play around with it again.
Working at UT may be the last time I work in an environment where I hesitate to just install something or don't have root access on servers?

In trying to get a working setup I hit a mind-boggling bug
in which I could not identify where a function was defined that was overwriting my custom "l" function.

Using `type l --detail` would only tell me that is was "sourced".
Managed to track down that this was happening in `/etc/fish/config.fish`
Which I would think is sourced first?

Realistically, I'd run into problems attempting to install zshell from source too,
but zsh is ubiquitous enough that I'd probably never NEED to install it on a machine I don't have root access to.
