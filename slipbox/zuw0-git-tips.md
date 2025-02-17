---
title: Git Tips
tags:
  - dev
---

## Big Repos

One of the big repos I interact with regularly is [nix](8m5l-nix-and-nixos.md).
It's a massive monorepo for all nixos packages which is both good and bad.

The bad is that a full git clone dumps 6GB on my hard-drive that I don't need, especially since I'm not working with the history in any way.

Some [instructions](https://discourse.nixos.org/t/nix-monorepo-size-and-contribution/5565/8) on the nixos discourse pointed me towards a possible solution which is `git worktrees`.

I promptly deleted my local `nixpkgs` git repo and re-cloned it as a bare repo.
I don't currently have any active PR's to edit but will evaluate this approach when I do.

I don't know that an analogue for this workflow exists in [`jj`](87f7-jujutsu.md).
