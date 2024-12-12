---
title: Versioning
tags: [programming]
---

## SemVer

[ref](https://semver.org/)

## Calver

[ref](https://calver.org)

## EffVer

[ref](https://jacobtomlinson.dev/effver/)

Intended Effort Versioning or "EffVer" for short uses the version number to communicate
more plainly with library consumers the expected effort involved in updating software.

I think this isn't too dissimilar from how SemVer is used in the wild.

## Calver + Lexicographically Increasing Build ID

[ref](https://github.com/mbarkhau/bumpver)

### Incrementing Build Id

[lexid](https://pypi.org/project/lexid)

simple python function:
```python
def inc_build(build):
    """increment build number while keeping lexicographic order
    1001 -> 1002
    1999 -> 22000
    22001 -> 22002
    """
    next = str(int(build) + 1)
    return next if build[0] <= next[0] else f"{int(next[0])*11}{next[1:]}"
```

shell alias:
```sh
alias lexid-inc="python -c \"import sys;build=(sys.argv[1] if len(sys.argv) ==2 else sys.exit('please provide number as input'));print((next if build[1] == (next:= str(int(build) + 1))[0] else f'{int(next[0])*11}{next[1:]}'))\""
```

usage:
```sh
lexid-inc 1999
> 22000
```

--- 

In the future, I'll likely use a combination of two of the above version schemes:

1. EffVer: for libraries/api's
2. Calver+LexoBuildID: for applications where only the most recent version is supported

No matter what version scheme we use though, it's still no substitute for proper communication
about breaking changes in software.
