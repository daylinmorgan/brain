---
title: Ploopy Adept
tags: [qmk, hardware]
---

Adept is a device sold by [Ploopy](https://ploopy.co), a small company working on open-source hardware.

The Adept is a trackball similar to something like a Kensington SlimBlade.
Since it's open-source, the folks at Ploopy maintain a
Github [repo](https://github.com/ploopyco/adept-trackball) that contains
all the files necessary to recreate the device.
I however, lack both the equipment (3D printer & soldering iron)
and the skill to build something like this myself.

I bought an assembled kit directly from them, which arrived in about two weeks.
Once I got it I wanted to modify the keymap/firmware in order
to enable something called drag-scroll toggle.

By default the firmware is compatible with VIA which allows for easy remapping.
But in order for the drag-scroll button to act as a toggle rather than a switch
a separate firmware needed to be loaded on to the device.

Ploopy takes advantage of `.uf2` files for firmware which
seem to automatically install themselves when copied onto the device.
They provide four different firmwares varying by drag-scroll sensitivity on their repo.
But when I first tried to install these I detected no change in the device.

In order to try to address this I opted to build the firmware myself using QMK.
Since I setup my current split keyboard with QMK I have switched to [nixos](8m5l-nix-and-nixos.md).
I first attempted to take advantage of the `shell.nix` included in the QMK repo.
Which started a long compilation of the QMK framework.
While waiting for that to finish I found out that QMK provides docker images and helper scripts
to run.
So once I enabled docker on my machine I proceeded with that.
Building the firmware followed the instructions provided by Ploopy and QMK but with a prepended helper script: 
`util/docker_cmd.sh make ploopyco/madromys/rev1_001:via`.
I copied over the resulting `.uf2` file and detected no change.

In order to achieve what I wanted I commented out [3 lines](https://github.com/qmk/qmk_firmware/blob/496d093fc32d992f8ef2a2823c5cc87f0a8e965c/keyboards/ploopyco/madromys/madromys.c#L43-L45) from `madromys.c`.
This achieved what I wanted and allowed the drag-scroll button to act as a toggle.

If I have time I may add a dedicated `madromys/keymap` to my `qmk` fork.
I think there should be some way to achieve what I did without editing the source, possibly with an `#undef`?
Or figure out how `qmk_userspace` works to separate my config from the main repo.



