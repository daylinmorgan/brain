---
title: Practical Nixos
tags: [python, nix]
---

A non-exhaustive list of the things I do to make NixOs work for me.
Because at the end of the day software purity is nice,
but I still need to actually get work done.

## Micromamba

Start a shell with a functional micromamba.

```sh
alias micromamba-fhs="nix-shell -E 'with import <nixpkgs> {}; (pkgs.buildFHSUserEnv {name = \"fhs\"; runScript=\"zsh\";}).env'"
```

## Existing Python Venv

[ref]: (https://nixos.org/manual/nixpkgs/stable/#how-to-consume-python-modules-using-pip-in-a-virtual-environment-like-i-am-used-to-on-other-operating-systems)

## Vscode

Just use `vscode-fhs` and move on with your life.

## Nix-ld


## Ongoing problems

### Python

Error from matplotlib:
```
ImportError: libstdc++.so.6: cannot open shared object file: No such file or directory
```

There are a number of ways to solve this the most attractive being to use nix-ld.
However, I run into an issues because qtile is corrupting the environment 
and taking precedence over the `python` wrapper that I add to `/run/current-system/sw/bin`.



