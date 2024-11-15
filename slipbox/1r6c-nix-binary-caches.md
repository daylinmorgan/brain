---
title: Nix Binary Caches
tags:
  - nix
  - selfhosting
---

While using `nix` I've frequently built and relied on in-development software.
This is sometimes using overlays or separate flakes without appropriate binary caches available.

I've used `cachix` for this in the past, see my cache [here](https://daylin.cachix.org).
This allows me to push any built nix closures to a place I can download them as I need.

However, since I'm using a free-tier I'm limited too 5GB.
Realistically, this is probably more than enough to effectively serve binaries that are at most downloaded 1 or 2 times.
But, I was still interested in the technical feasibility of a self-hosting option.
This way I can still have a binary cache in the event that `cachix` is less generous in the future.

So, using my VPS at hetzner I now have a personal cache managed with [attic](https://github.com/zhaofengli/attic).
This also means I have yet another [subdomain](mqnm-subdomains.md) at [attic.dayl.in](https://attic.dayl.in).

Now when my update job on GHA hits a cache miss it build and pushes to `https://attic.dayl.in/oizys`.
For now the storage backend is a sqlite database but in the future I may explore using `postgres` or hosting the storage a [different backend][backend-ref].


## Issues I've had

When a cache becomes unreachable nix just straight up errors about it for no good reason.
Need to track down the flags to convince it to not check a single substituter that might be offline.

Otherwise I may hit "chicken/egg" problems when `algiz` both hosts the cache and uses it.

[backend-ref]: https://lgug2z.com/articles/deploying-a-cloudflare-r2-backed-nix-binary-cache-attic-on-fly-io/
