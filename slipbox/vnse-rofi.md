---
title: Rofi
tags:
  - linux
---

[Rofi](https://github.com/davatorium/rofi) is an awesome tool to replace many of the functionalities in a fully-fledged desktop environment.


## Tips

### Reset item in dmenu frequency sorting

One of the main ways I use rofi is as an app launcher.
Sometimes I switch the primary application I use for instance switching to Firefox while keeping Chrome installed.
To prevent muscle memory from opening the main app I launch from Rofi I need to reset's its ranking in the `+dmenu` rofi interface.

A simple way to do this is to open rofi place the selector on the item and use `Shift + Delete`.

To manage the drun frequency more you can directly edit the file `~/.cache/rofi3.druncache`.
Either delete the whole file or manually edit individual lines.

For instance reset the counter for a specific application:

```sh
sed -i '/google-chrome\.desktop/d' ~/.cache/rofi3.druncache
```

