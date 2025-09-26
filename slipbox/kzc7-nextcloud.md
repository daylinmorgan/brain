---
title: Nextcloud
tags:
- devlog
- selfhosting
---

## Installing Nextcloud with Docker

I basically just used the nextcloud all-in-one docker container.
It was then up and running and behind a caddy reverse proxy.

---

## Accessing files using rclone

In order to access files with rclone it uses a standard protocol called [WebDAV](https://docs.nextcloud.com/server/latest/user_manual/en/files/access_webdav.html).

These docs (and rclone after my first failed attempt) suggest the "URL" used for configuration should be `https://cloud.example.com/remote.php/dav/files/USERNAME/`

or in my case `https://cloud.dayl.in/remote.php/dav/files/daylin`.

After setting this up I now have an `rclone` accessible cloud storage independent of big tech unfortunately, it is dependent on small tech (me for admin and the open source community for the real hard work).

While setting up this remote I learned that you can also configure "alias" remotes so setup the actual remote as `nextcloud:` and a shorter alias with `nc:`

---

## Editing Files

I attempted to open a `.docx` from the files already present and it failed to open Collabora, complaining about socket misconfiguration.

Error:

> Failed to establish socket connection or socket connection closed unexpectedly.
> The reverse proxy might be misconfigured, please contact the administrator.
> For more info on proxy configuration please checkout https://sdk.collaboraonline.com/docs/installation/Proxy_settings.html

Based on this [thread](https://github.com/nextcloud/all-in-one/discussions/1358)
I added the server for my IP to the allow list for WOPI requests on the page at <https://cloud.dayl.in/settings/admin/richdocuments>.

I still couldn't open any files using Collabora, so I tried to use the "insecure" route by adding 0.0.0.0 to the list but that also didn't seem to resolve the issue.
After including 0.0.0.0 in the list it just seemed to hang, so I removed both of the I.P. addresses I added.

I next tried to switch to using a collabora demo server but that also seems to fail inexplicably.

Trying to reinstall the collabora container after disabling seccomp

---

While trying to get this to work I seem to have run out of diskspace.
Thus confirming for me I'm not ready for this type of solution.
I then stopped and pruned all nextcloud containers and tediously removed each docker volume.
