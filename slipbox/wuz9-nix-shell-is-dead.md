---
title: Nix-shell is dead
tags: [nix]
---

By the time I started using [`nixos`](8m5l-nix-and-nixos.md) there was a deviation of UX/design choices.
Alongside flakes there is an effort to stabilize the CLI around subcommands
rather than the typical multi-executable approach originally taken.

Currently, this is locked behind a feature flag enabled with `experimental-features = nix-command`
Ironically, the naming here uses a hyphenated word.


I have an [alias](euqd-practical-nixos.md) around `nix-shell` in order to invoke micromamba in a FHS

[ref](https://blog.ysndr.de/posts/guides/2021-12-01-nix-shells/)


