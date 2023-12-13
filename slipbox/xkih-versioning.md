---
title: Versioning
tags: [programming]
---

## Semver

[ref](https://semver.org/)

## Calver

[ref](https://calver.org)

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

