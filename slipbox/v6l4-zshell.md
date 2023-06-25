---
title: Zshell
tags: [shell]
---

# Zshell

## File Name Manipulation

Zsh file name without the extension
Zsh provides a weird way to get the different parts a of a file name.

If you want the full path without the extension:
```zsh
> myfile=/path/to/story.txt
> echo ${myfile:r}
/path/to/story
> myfile=story.txt
> echo ${myfile:r}
story
```

If you want just the file name minus the path:
```zsh
> myfile=/path/to/story.txt
> echo ${myfile:t}
story.txt
```
Check this out you can combine those two symbols!

```zsh
> myfile=/path/to/story.txt
> echo ${myfile:t:r}
story
```

Get a symlink resolved directory name in order to get the current directory name and it's parent.
I use this in my `tn` shell function new as a backup if no argument supplied.

```zsh
$PWD(:A:t2)
```

