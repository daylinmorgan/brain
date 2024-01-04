---
title: Practical Nixos
tags: [python, nix]
---


## Micromamba

Start a shell with a functional micromamba.

```sh
alias micromamba-fhs="nix-shell -E 'with import <nixpkgs> {}; (pkgs.buildFHSUserEnv {name = \"fhs\"; runScript=\"zsh\";}).env'"
```

## Existing Python Venv

[ref]: (https://nixos.org/manual/nixpkgs/stable/#how-to-consume-python-modules-using-pip-in-a-virtual-environment-like-i-am-used-to-on-other-operating-systems)


