---
title: Nix Hash Mismatch
tags: [nix]
---


[Nix](8m5l-nix-and-nixos.md) has been a boon to my system stability and reliability.

Thanks to how easy `nixos` makes it I fearlessly rely on unreleased software, at the time of writing: `lix`, `roc` and `zig`/`zls`.
In order to not wait around for compilation when I bump my dependency locks I utilized github actions and cachix.

However, on more than one occasion I've been plagued by an issue in which packages built and cached from github actions are still rebuilt
locally.
While this isn't the end of the world it's beneficial to determine why a derivation is unstable and how I can ensure reproducible outputs.
To my knowledge so long as the system (i.e. x86_64-linux) is the same the compilation should be as well.

As a test case, I'm going to attempt to track down why `zigtools/zls` which is build from a flake is not hitting the cache.

hash from github action build: `rcmajvsz4mm5pqz1ka419876f2061afc`
hash after `oizys update` build: `z1j56vyay093h7hlxza3fj8zzn25bcdr`

Downloaded version built by GHA with the below command:

```sh
nix-store -r /nix/store/xqgpbk8zjr6p41m9v0vjamxsbkwmqa3q-zls --substituters 'https://daylin.cachix.org' --trusted-public-keys 'daylin.cachix.org-1:fLdSnbhKjtOVea6H9KqXeir+PyhO+sDSPhEW66ClE/k=' -vvvv
```

The dependencies shown by `nix-store --query --tree /path/to/closure` are the same.
It's possible the issue is something to do with their `src` which uses `hercules-ci/gitignore`
Or it's due to the `zon2nix` deps closure.

~~Based on [this](https://nix.dev/guides/best-practices#reproducible-source-paths) it seems like the issue might arise in how they specify the `src = gitignoreSource ./.;`~~. Actually, this is describing that if you move this to a different place then it's now hash-<name of dir>.
But in this case the name of the directory doesn't change.

Back to thinking the culprit is the zon2nix business somehow.

