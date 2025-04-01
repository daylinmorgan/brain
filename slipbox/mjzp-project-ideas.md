---
title: Project Ideas
tags:
  - dev
---

Frequently, I think up problems I'd like solved (either by myself) or someone else.
This is a collection of ideas for things that I think would be either interesting to work on or helpful for my own workflow.

## llm-tui

I use [llm](https://github.com/simonw/llm) more than I thought I would and I sometimes wish I had a tui for the chat interface.
I think with something like [textual](https://github.com/Textualize/textual) and the plugin api of llm, this would be pretty doable to implement in a few days.

### features

- input box
- response box (with optional markdown rendering)
- model selector
- existing conversation selector


## nimblex

A nim "script" runner

### features

- meant to be used as with a shebang
- configurable (location, gcc, nim path, extra nim config file location)
- generates nimble paths based on deps similar to viv
- computes two hashes, one for deps block and one for script
- implement env handling or use TMPDIR

### usage

```sh
nimblex run --mode ephemeral ./script.nim
nimblex run ./script.nim
nimblex env list
nimblex env remove
```

### Prior Art

- [nimrun](https://github.com/flaviut/nimrun)
- [nimr](ihttps://github.com/Jeff-Ciesielski/nimr)
