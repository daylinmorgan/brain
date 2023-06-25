---
title: Zstyle
tags: [zsh, unix]
---

# Zstyle

For manpage: `man zshmodules`

From this [SO](https://unix.stackexchange.com/questions/214657/what-does-zstyle-do)

```sh
# reference: http://zsh.sourceforge.net/Doc/Release/Zsh-Modules.html#The-zsh_002fzutil-Module

# list all zstyle settings
zstyle -L

# store value in zstyle
zstyle :example:favorites fruit apple

# store multiple values in zstyle
zstyle :example:list fruits banana mango pear

# retrieve from zstyle and assign new $fav variable with -g
zstyle -g fav ':example:favorites' fruit && echo $fav

# retrieve from zstyle and be explicit about the assignment data type:
# -a: array, -b: boolean, -s: string
zstyle -a :example:list fruits myfruitlist && echo $myfruitlist

# test that a zstyle value exists with -t
if zstyle -t ':example:favorites' 'fruit' 'apple'; then
  echo "an apple a day keeps the dr. away"
fi
if ! zstyle -t ':example:favorites:vegtable' 'broccoli' 'no'; then
  echo "Broccoli is the deadliest plant on Earth - why, it tries to warn you itself with its terrible taste"
fi

# delete a value with -d
zstyle -d ':example:favorites' 'fruit'

# list only zstyle settings for a certain pattern
zstyle -L ':example:favorites*'
```
