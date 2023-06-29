---
title: Search for Static Sites
tags: [meta]
---

# Search for Static Sites

Search is an obvious quality of life improvement to a website primarily consisting of information.
Such as this very `brain`!

Thus, I embarked to add a [search](/search) feature to my own zettelkasten theme `brain stem`.
The developers of `hugo`, to their credit, shout out a few options in their [documentation](https://gohugo.io/tools/search/).
So I tried to find more information on a basic implementation with `lunr.js`.
This led me to a [blog](https://victoria.dev/blog/add-search-to-hugo-static-sites-with-lunr/)
with info about how to implement this with the addition of only a few files.

Using this blog as a guide I managed to get a working search with `lunr`.
This would be fine but then I discovered the most recent commit was from [2020](https://github.com/olivernn/lunr.js/commit/aa5a878f62a6bba1e8e5b95714899e17e8150b38)😱.
While this in itself is probably not a big deal assuming the basic feature set is covered,
I have an unreasonable fear of "unmaintained" projects.

Looking for an alternative with a similar use case and feature set led me to [`minisearch`](https://lucaong.github.io/minisearch/).
Thus, I then further adapted my own layouts/js to use `minisearch` instead.

Given the options around I feel motivated to maybe generalize this feature set to a separate `hugo` module.
My main trepidation is that I style everything using `unocss` making it less usable for anyone using vanilla css.

The one unexpected caveat of any of these implementations is that the
website needs to have at least a blank file at `./content/search/_index.md`

Relevant Commits:
- [yay lunr.js](https://github.com/daylinmorgan/brain-stem/tree/d92e250f7f4787cbed936ffec3864631e6078d13)
- [lunr.js is dead long live minisearch](https://github.com/daylinmorgan/brain-stem/tree/3c2a7f3321144c8b75bba8a1a1b48d8038e8545e)


