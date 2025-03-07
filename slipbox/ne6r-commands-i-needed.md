---
title: Commands I needed one time
tags:
  - dev
---

This is a list of commands I need once and got either from sleuthing or LLM's that
if I need more than once or twice I should probably make them a [zsh function](v6l4-zshell.md).

## Compression with progress

I had to compress a very large analysis for work (> 200GB) and wanted to both effectively compress it and view progress.
Discovered two important components xz takes a thread argument (-T0) for all threads, and pv for progress viewing.

```cmd
tar cf - analysis --dereference | pv -s $(du -sb analysis | awk '{print $1}') | xz -T 20 > analysis.tar.xz
```

I imagine the call to awk is unnecessary and there is a simpler way to extract total size.
Also found out `pv` is not a GNU Coreutil so needed a [nix-shell](wuz9-nix-shell-is-dead.md) to test locally.

