---
title: Nix Binary Caches
tags:
  - nix
  - selfhosting
  - todo
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
For now the storage backend is a sqlite database but in the future I may explore using `postgres` or hosting the storage at a [different backend][backend-ref].

Given that a lot of the binaries I cache myself (namely lix-HEAD) is also used by `algiz`.
It might be worthwhile to instead piggy back on the existing `/nix/store/` and try one of the several nix store as a binary cache solutions, such as [harmonia](https://github.com/nix-community/harmonia) or [nix-serve-ng](https://github.com/aristanetworks/nix-serve-ng).
I think this would mean that to populate the cache from GHA I would need to manually copy the closures using `oizys`/`nix-copy-closure`.
And again setup ssh access within the GHAs.

Update:

I've setup harmonia on `algiz` and integrated `nix-copy-closure` into `oizys cache` if the "type" of cache is set to "store".
I'll run this setup for awhile and check back in occasionally on the size of the /nix/store.
It would probably be useful to write my own monitoring script to track how the store changes in terms of size and number of closures.
Ideally, it should have some steady-state or else it needs more aggressive garbage collection.

There is a possibility if I build something using GHA and don't bother to rebuild my systems soon enough that it will get cleared from the store.
I could prevent this by server side maintaining GC roots but this sounds more complicated.
I think at that point I'd be better off returning to using attic for cache purposes.

Update:

After using harmonia for a while, I have had no issues with pusing to the cache.
However, I do think the inability to easily prevent garbage collection based on something seperate from my VPS settings is problematic.
This did come up at least once which is frustrating.
It's also probably the case that storing closures directly in the `/nix/store` is less space efficient.
Since, I'm not interested in manually handling GC roots, I've decided to go back to relying on attic for my nix build caching.

## Issues I've had

When a cache becomes unreachable nix just straight up errors about it for no good reason.
Need to track down the flags to convince it to not check a single substituter that might be offline.

Otherwise I may hit "chicken/egg" problems when `algiz` both hosts the cache and uses it.

Nix is poor at handling what to do when a cache it expects to be online isn't. In some cases it basically just spits out TLS errors and aborts the build.
A good enough workaround especially for something that is relatively easy to build is to enable the build fallback.
To add this option to `nix` append any command with `--option fallback true`

[backend-ref]: https://lgug2z.com/articles/deploying-a-cloudflare-r2-backed-nix-binary-cache-attic-on-fly-io/
