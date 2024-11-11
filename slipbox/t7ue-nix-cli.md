---
title: Nix Garbage
tags:
- nix
- linux
---

## Nixos generations

[Deleting old generations](https://discourse.nixos.org/t/list-and-delete-nixos-generations/29637/2)
tldr: `nix profile history`

Simplest strategy go to `/nix/var/nix/profiles/` delete symlinks, then run `nix store gc`.

Could be nice to make an interactive in `oizys` to choose profiles, delete profiles, then ask about garbage collection.

Help:
- `man nix3-profile-history`
- `man nix3-profile-wipe-history`

## Finding GC roots

To see why a path in the nix-store isn't being deleted:

1. Use `nix-store --query --referrers /nix/store/path`
2. Check for live references with `nix-store --gc --print-roots`
3. Examine GC roots in /nix/var/nix/gcroots/
4. Look for indirect roots with `nix-store --indirect --add-root`

These commands will help identify what's keeping the path alive.
