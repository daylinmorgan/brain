---
title: Connecting to the UTVPN
tags: [vpn, linux]
---

UT made a change to their DUO authentication which broke my ability to connect to vpn.utexas.edu.

This is the series of steps that lead me to a semi-working solution.

First I confirmed the VPN was functional.

Switched to windows and discovered:

- the builtin vpn in windows 10 was not working
- downloaded the official cisco client
- found out the authentication launches a browser now
- first attempt was blocked by a cryptic error message about detecting an attack
- second attempt was successful

`othalan` + Cisco:

- tried to install the official client which ships as an 8MB "shell script" (probably java application)
- unsurprisingly installation failed as it unpacks to `/opt/cisco/` and proceeds to 
  try to copy things into the root file system which are read-only...because [NixOS](8m5l-nix-and-nixos.md)
- ignored those since it mostly looked like icon data (but there were some [systemd](dhef-systemd-service-files.md) files)
- tried to launch `/opt/cisco/anyconnect/bin/vpnui` anyways and it didn't work
  - probably some shared library issues or maybe a lack of daemon that was supposed to be launched by systemd)

`othalan` + openconnect:

Suspected issue: openconnect needs to launch a browser for me to authenticate.
Looking around online this may be related to the useragent?

Tried this command:

```sh
openconnect vpn.utexas.edu --useragent=AnyConnect
```

Successfully opens the browser,
first attempt leads to the same cryptic error about detecting an attack. 
So I closed all the open browser windows and tried again.
On the second attempt authentication was successful
However, since I started it as a regular user it failed to write to `/var/run/vpnc`.

Tried to launch the above command as sudo but then `xdg-open`
tries every browser under the sun except my current browser `vivaldi`.

Tried to create the directory it needed but it still failed with some other error.

Wanting to avoid trying to convince `xdg-open` to work for root,
which I figured would be more hassle than it's worth,
searching led to the official documentation on
[running as a non-root user](https://www.infradead.org/openconnect/nonroot.html)


This suggest the following bash script:

```bash
#!/bin/bash

COOKIE=
eval `openconnect --authenticate "$@"`
if [ -z "$COOKIE" ]; then
    exit 1
fi

sudo openconnect --servercert "$FINGERPRINT" "$CONNECT_URL" --cookie-on-stdin ${RESOLVE:+--resolve "$RESOLVE"} <<< "$COOKIE"
```

Using a cookie like this means I can launch the browser to authenticate
and then perform the actual connection itself as `root`.
This works and for now I'll replace my existing `utvpn` expect script with
a derivation of the above setting the default args rather than evaluating with `"$@"`.
