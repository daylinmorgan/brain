---
title: TTY Fonts
tags: [linux]
---

# TTY Fonts

The default console font is pathetically hard to read on hi-res screens of now.

This can be corrected with installation of `terminus-fonts`.

```dosini
FONT=ter-p32b
```

*Note*: the "b" at the end is for bold

If one finds themselves spending time in the virtual console and 
needs a smaller font this can be returned to defaults with an argument-free call to `setfont`.

