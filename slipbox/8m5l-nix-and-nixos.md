---
title: Nix and Nixos
tags:
  - nix
  - linux
---

Nix could be used to describe the `nix` command line program or `nix` the language.

Nixos is a declarative operating system built atop both of these components.

The idea of `nix` and Nixos for fully declarative and *mostly* reproducible 
system management is quite appealing.
For me personally, I find more benefits in it's system management than package management.
I've not really had issues with up-to-date functioning packages on Arch Linux mostly thanks to the AUR.

Because of how Nixos works many packages require workarounds or patches to
overcome historical expectations about how libraries or applications are available on a system.

At some point I switched my server hosting `https://git.dayl.in` to use `nixos`.
It has worked well for system management. Crucial application packages have still been handled using `docker`.
But given many of the packages I use are essentially binary applications
(from go: gitea, caddy, soft-serve, from rust: lemmy) I could probably
leverage `nix flakes` to host these services as well.

## Headaches

A commit to how `nim` handles `dlload` on Nixos highlighted to me that I haven't fully drank the kool-aid on `nix`.

Simply compiling `nim` packages that depend on `openssl`,
which is essentially any package interfacing with `https` has now changed.
It's impossible to do so without opening a shell with access to
[shared libraries](https://nixos.wiki/wiki/FAQ/I_installed_a_library_but_my_compiler_is_not_finding_it._Why%3F).

I can see the merits for this change but it still demonstrates to me a way in which using Nixos
for the forseeable future and likely for as long as it exists will require these types
of cognitive shifts to a slightly different way of doing things.
But of course, what's gained particularly for applications is a less obfuscated build.

## Syntax

Caveat I've found editing my system configuration is to always err on the side of more syntactical sugar.
For example when writing functions or imports add the parenthesis or brackets that indicate structure.
Otherwise, you are likely to get odd recursion errors which fail to spell out the actual problem.

## Contributing

Adding to nixpkgs is relatively straightforward and to find out where in the stages/channels a particular PR is there
is a handy online [tracker](https://nixpk.gs/pr-tracker.html).
