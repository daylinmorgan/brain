---
title: Ghostty
tags: [dev, terminal]
---


Things I had to workaround in the beta ghostty phase:


My window manager uses a "float editor" class to determine that windows should float.
I use this for a few keybinds that load up vim or other apps for quick edits.

Unexpectedly this wasn't working and based on conversations on the Ghostty discord it seems the issue comes down to GTK requiring a period in the name?
I thought I would submit a PR with this info pointing to the GTK docs, but it turns out I don't read...this info was already included.

Using a period in the name indeed properly set the class.

The other thing I found on the same thread is GTK does not support server-side cursors. Which would include hyprcursor, meaning if I want to change the cursor I'll need to go through GTK.

Eventually will probably involve editing `~/.config/gtk-4.0/settings.ini` or running this command: `gsettings set org.gnome.desktop.interface cursor-theme {theme name}`.
