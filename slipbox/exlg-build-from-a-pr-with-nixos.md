---
title: Build From A PR with NixOS
tags:
- linux
- nix
---


Even though I use [NixOS](8m5l-nix-and-nixos.md) and run `nixos-unstable`.
There is occasionally slow to merge PR's either because of thorough review or build infrastructure.

It's fairly straightforward to test simple packages that aren't deeply integrated with the OS level for functionality.

As an example, I wanted to try out v4 of `fish` but it had yet to be released luckily this (at the time) draft [PR](https://github.com/NixOS/nixpkgs/pull/367229) already had a working derivation.

To use this on `othalan` and with `oizys` I made the following changes:

1. Added a flake input:

```nix
nixpkgs-fish-pr = "github:nixos/nixpkgs/fish;"
```

2. Added this nixpkgs as an attribute to `nixpkgs` using an overlay:

```nix
(final: prev: {
  nixpkgs-fish-pr = import inputs.nixpkgs-fish-pr {
    system = final.system;
  };
})
```

3. Referenced this package in my host config for `othalan`:

```nix
environment.systemPackages = [ pkgs.nixpkgs-fish-pr.fish ];
```

