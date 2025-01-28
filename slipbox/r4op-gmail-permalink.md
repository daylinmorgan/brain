---
title: GMail Permalink
tags:
  - web
  - email
---

I have several gmail accounts and the "inbox" url shifts according to the order in which they were authenticated i.e. the `0` in this url shifts:
`https://mail.google.com/mail/u/0/#inbox`.

In order to create stable links (like for a usable bookmark) you need to use a url of the form:

```
https://mail.google.com/mail/u/?authuser=user@gmail.com
```

This link will direct to the correct inbox. Hopefully this option never goes away on Google's end.
