---
title: Practical Nixos
tags: [python, nix]
---

A non-exhaustive list of the things I do to make NixOS work for me.
Because at the end of the day software purity is nice,
but I still need to actually get work done.

## Get NixOS to check my recently populated cache

[narinfo-cache-negative-ttl](https://nix.dev/manual/nix/2.22/command-ref/conf-file.html#conf-narinfo-cache-negative-ttl)

## Get the originating flake info for a running system-path

```sh
nix-store -q --deriver /run/current-system | nix flake metadata
```

## Building only the 'system-path'

Get the 'system-path' store path

```sh
nix derivation show `oizys output` | jq -r '.[].inputDrvs | with_entries(select(.key|match("system-path";"i"))) | keys | .[]'
```

Build the 'system-path'

```sh
nix build '/path/to/system-path.drv^*' --log-lines 0 --print-build-logs
```

## Keeping a clean system

`nix store gc` and `nix-collect-garbage` will only remove things that do not have `gcroots`.
`gcroots` are a sort of file-system usage indicator nix uses to know a store path should be kept around.

Since I use `nix-direnv` these can build up over time, but I found out [`nh`](https://github.com/nix-community/nh)(a sort of `oizys` competitor) has a clean command.
But even better it has a nixos module which I enabled like this:

```nix
programs.nh = enabled // {
    clean = enabled;
  };
```


## Micromamba

Start a shell with a functional micromamba.

```sh
alias micromamba-fhs="nix-shell -E 'with import <nixpkgs> {}; (pkgs.buildFHSUserEnv {name = \"fhs\"; runScript=\"zsh\";}).env'"
```

## Existing Python Venv

[ref]: (https://nixos.org/manual/nixpkgs/stable/#how-to-consume-python-modules-using-pip-in-a-virtual-environment-like-i-am-used-to-on-other-operating-systems)

## Vscode

Just use `vscode-fhs` and move on with your life.

## Distrobox

I made a custom [distrobox](https://git.dayl.in/daylin/daylinbox) as one of the ultimate fallbacks.


## Build Failures

If I am suddenly needing to build something that is usually built by `nixos` I need to check if build failures are happening on hydra.
If they aren't it means I've changed the closure somehow, otherwise the error is upstream and should in theory be resolved eventually.

The ui for hydra is kind of a nightmare. But there is [`hydra-check`](https://github.com/nix-community/hydra-check) for the fastest check of single package.

## Make warnings more serious

They deprecated the `pkgs.system` alias.
Which means I'm now constantly playing whack-a-mole with this message:

```
trace: evaluation warning: 'system' has been renamed to/replaced by 'stdenv.hostPlatform.system'
```

This command will hopefully give you a decent enough stack trace to track it down:

```sh
NIX_ABORT_ON_WARN=true nix build `oizys output` --dry-run --show-trace --impure
```

## Ongoing problems

### Python

Error from matplotlib:

```txt
ImportError: libstdc++.so.6: cannot open shared object file: No such file or directory
```

There are a number of ways to solve this the most attractive being to use nix-ld.
However, I run into an issues because qtile is corrupting the environment 
and taking precedence over the `python` wrapper that I add to `/run/current-system/sw/bin`.



