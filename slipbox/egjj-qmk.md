---
title: QMK
tags:
  - peripherals
  - keyboards
---

My first exposure to [qmk](https://qmk.fm/) was in modifying my planck ez from [zsa](https://zsa.io).

Since then I've also made use of qmk for customizing the experience of my corne keyboard and [ploopy adept trackball](2ffh-ploopy-adept.md).

Originally I made use of qmk through a fork. Since then they've added support for something called "userspace".
I've opted to move my configs over to this to facilitate better organization and deliniation from builtin keyboards/keymaps.

Under the new setup I need to have two directories locally `qmk_firmware` and `qmk_userspace`.

```sh
jj git clone git@github.com:qmk/qmk_firmware.git
jj git clone ssh://git@git.dayl.in/daylin/qmk_userspace.git
```

Next we need to make sure that `qmk` can find the needed setups:

```sh
nix-shell -p qmk --command zsh
qmk config user.qmk_home=$PWD/qmk_firmware
qmk config user.overlay_dir=$PWD/qmk_userspace
```

Following this we can enter the userspace directory and build any keymaps:

```sh
cd qmk_userspace
make ploopy/madromys:daylinmorgan
```

