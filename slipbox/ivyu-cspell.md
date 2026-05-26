---
title: Cspell
tags:
  - writing
---

When writing prose, it's useful to have at a minimum a spell checker.
Particularly in the case of these writings and other similar endeavors in which I'm writing prose through a text editor I make use of [cspell](https://cspell.org).

Typically, my setup includes a custom dictionary maintained at the project root in a plaintext file `dict.txt` and a basic config to expose it to cspell at .cspell.config.yaml

```yaml
$schema: https://raw.githubusercontent.com/streetsidesoftware/cspell/main/cspell.schema.json
version: '0.2'
dictionaryDefinitions:
  - name: dict
    path: './dict.txt'
    addWords: true
dictionaries:
  - dict
ignorePaths:
  - 'node_modules'
  - '/dict.txt'
```

Then to use it files can be checked with `cspell lint [path]`.

