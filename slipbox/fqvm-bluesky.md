---
title: Bluesky
tags:
- dev
- selfhosting
- fediverse
---

I previously set up a bluesky PDS. But got less optimistic about its longevity.
For many unsurprising reasons it seems to be gaining traction faster than mastodon.
So to remain apart of the network effect I'll attempt to revive my PDS from it's existing implementation.


I'm mostly concerned that having come online I can't just spin up a new identity willy-nilly,
but I'm not totally sure how the AT Protocol handles name changes.

But as long as I can still claim the @dayl.in handle then I'm not concerned with preserving data.

## What still exists on `algiz`?

The following `docker-compose.yaml` was previously used:

```
services:
  pds:
    container_name: pds
    image: ghcr.io/bluesky-social/pds:0.4
    restart: unless-stopped
    volumes:
      - ./pds:/pds
    env_file:
      - ./pds/pds.env
    networks:
      - caddy

networks:
  caddy:
    external: true
```

The current release of `bluesky-social/pds` is still `0.4.74`.
I wish I would have bothered to use a more specific image, but either way I first removed the networking config and exposed the internal ports.

Steps I eventually took to get back online:

- Added an entry in my `Caddyfile` in oizys config
- Set up DNS again for both `bksy.dayl.in` and `daylin.bsky.dayl.in`
- Added back a TXT record for `_atproto.dayl.in`

I think not having a DNS record at `daylin.bsky.dayl.in` or having `caddy` reverse proxy this domain is what prevented my PDS from functioning correctly.
Case in point my "hello world" post seems to have never entered the network and became visible after what should have been my second post regarding "invalid handle".

Now to see how much this database grows. I expect that given my minimal posting and primarily text-based interactions that the PDS will remain small much like go-to-social.
