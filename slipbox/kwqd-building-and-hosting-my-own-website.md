---
title: Building and hosting my own website
tags:
  - devlog
---

As of writing (2025.08.27), my personal website at <https://dayl.in> is built and hosted using GitHub.

I think that for now GitHub is not going anywhere and while I use it for a lot of my OSS projects, there isn't really a need for me to use it for things I'm the sole contributor to.
If I just want it to be publicly accessible then their are other options.
For hosting the repo at least the best option is my own git server at <https://git.dayl.in>. 
Below I want to explore some alternatives for hosting the site itself.

## Self-host

One option would be to simply build and host the site myself on `algiz`.
This should be rather straightforward since I already use `caddy`.
I could additionally build the website with `nix` then pull in the repo as a `nix flake` input to `oizys`.
Then the "build" of the website would only be as needed and handled automatically with a deployment of `algiz`.

## Commercial

There are a number of free commercial static hosting options.
A problem I have with alot of these options is that they are doing too much.
For something like this website where I build it a couple times a year I don't need complex build offerings.
A simple rsync of built files would be sufficient.

I think for any commercial option it's fine if some years down the road I need to migrate.
The less overhead (custom pipeline files, logins, etc.) a service has to use the easier it is form me to jump ship later down the road.

### [GitHub Pages](https://docs.github.com/en/pages)

What I use now but don't want to because Microsoft....enough said.

### [Codeberg Pages](https://docs.codeberg.org/codeberg-pages/)

Codeberg technically can host static sites but the future of the offering seems murky at best.

### [Netlify](https://www.netlify.com/)

Netlify has a free offering but billing horror stories give me pause.

### [Cloudflare Pages](https://pages.cloudflare.com/)

There free plan seems good enough for my needs:

>  1 build at a time
>  500 builds per month
>  100 custom domains per project
>  Unlimited sites
>  Unlimited static requests
>  Unlimited bandwidth

The website suggests starting with something they call "Workers", which bills more so by usage.

>Free
>100,000 requests per day
>(Across all of your Worker scripts, UTC+0)
>
>    Deploy up to 100 Worker scripts
>    Runs on all 275+ network locations
>    Free workers.dev subdomain
>    Free static asset requests
>    Up to 10ms CPU time per request
>    Lowest latency after the first request
>    Up to 3,000 build minutes per month
>    1 concurrent build slot
>    Limited Workers KV edge storage

This makes it seem like Cloudflare pages could be deprecated in the future.


### [Vercel](https://vercel.com/)

Vercel's "hobby" plan offering seem more generous than others.
Similar to Netlify it really has a feel that small-time customers are not the target.

### [Surge](https://surge.sh/)

This one seems really interesting as a hyper-dedicated service around the notion of static website hosting.
There free plan is also quite generous, which they recognize and are committed to.

## Testing surge

I added surge to my devDependencies and ran `surge`.
I typed in an email and password and it auto-selected a {subdomain}.surge.sh.

After running and going to the link I realized I just ran this from the project root directory and likely did not actually publish built assets..whoops.
I then reran this command and specified the path for the built site at `./dist`.

This time it worked just fine and successfully published the site, at a different subdomain.

I do find it mildly concerning that when poking around the site (and in official emails) there are dead image links.
It gives the impression (however superficial) that the service is, at the very least, maintained with minimal support.

## Build with nix, deploy with Caddy

This is the homegrown option which makes all the problems my own.
No third-party build pipeline software, no hosting.
Just me building a website and serving it myself, oh boy.

First I need to work out the "build" step (with nix, yay.)
This seems like a chance to swap the node package manager to bun.
Seems like their is poor `pnpm` support in the first place with `nix`.

---

In the end, for now I implemented the solution using `nix` and integrated my site as a "service" on `algiz` hosted using caddy.
