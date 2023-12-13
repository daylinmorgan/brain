---
title: Paths are weird
tags: [shell, zsh]
---

Working on unix one eventually becomes intimately familiar with the `$PATH`.

In [zsh](v6l4-zshell.md), the `$PATH` variable is mirrored to a `$path` variable as an array.
Which to me, is nicer to work with and make more sense.

In addition with zsh one can keep only the first occurrence of duplicated values with `typeset -U path`. See `man --pager='less -p "typeset -U"' zshbuiltins` for more info.

