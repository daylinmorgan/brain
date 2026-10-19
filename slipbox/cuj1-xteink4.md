---
title: Xteink X4
tags:
- device
- todo
- bug
---


When reading an `epub` on my XTEINK4 I noticed some of the text that should have been bold wasn't.
Upon investigation of the underlying stylesheets of 2 `epub`'s I realized that in the working one font-weight was specified as `bold` vs the non-working one:

```css
.class {
  font-weight: 800;
}
```

To fix this I appended another rule to the stylesheet:

```css
.class_a, .class_b ... , .class_z {
  font-weight: bold;
}
```

I thought this might fix the issue but it didn't seem like it.
