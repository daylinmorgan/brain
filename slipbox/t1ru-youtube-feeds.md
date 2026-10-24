---
title: Youtube Feeds
tags:
- devlog
---

I use youtube alot!

I also tend to watch a lot of long-form content that I may not be able to watch when it comes out.
I've attempted to manually curate some of this content into categorical playlists, but it's difficult to stay on top of new releases.

It would be nice if Youtube had a custom feed mechanism (that isn't [slotware](https://support.google.com/youtube/answer/17081258?hl=en))
to allow me to curate sets of channels that I can consume at my leisure.

In my ideal world I could run some alternative Youtube front-end based on these curation mechanisms, that could allow channel or video tagging and custom sorting.
Something tells me Alphabet wouldn't look to kindly on that.

I think my best bet is just going to be aggressive playlist curation.
Playlists kinda suck as an interface for this especially because they combine with youtube music which is in my opinion a bad UI.
But I do think a viable option and one that is less investment is using Google Apps Script to handle my playlists curation.

Searching around I found a possible solution in [Subplayo](https://github.com/Tholdrim/Subplayo).

## Setting up Subplayo

I followed the instructions on the README and setup a Google Apps Script project with the source and files.
Then I cloned it locally using `clasp` and discovered that of course to move files I have to use the UI.

However having them locally makes it much easier (for me at least) to update the `Settings.js` with my playlists and videos.

Apps script is nice since you set timers (which I've done for [gmail scripts](9jn5-gmail.md)) and run on google hardware.

## Future Directions

Ways to implement my ideal solution:

Collect tracking data via the RSS feed (can poll more this more often but has limited data).
Collect historic or granular video information via YT API.

Requirements:

- daemon to keep db of videos current
- credentials to access YT API
- frontend to view feeds

Because of the quota system of the Youtube API this could work as a self-hosted service.
I think I would also need to handle some sort of auth/user system, this could be an end-goal.
Though practically I think this would be the most difficult for me to implement.
