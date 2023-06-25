---
title: Systemd Service Files
tags: [linux]
---

# Systemd Service Files

Files used to interact with systemd.

There are additional tools on the horizon to replace systemd,
but it has remained standard and likely will for the foreseeable future.

One use case of defining your own systemd file is
to trigger a third-party screen lock based on system events.


I have written a custom "lock" script which wraps i3lock-color.
Without a custom script one could use `/usr/bin/i3lock` as the `ExecStart`.

The below file could saved at `/etc/systemd/system/i3lock.service`.

Enabling it requires running `sudo systemctl enable i3lock.service`.

Now whenever the system is triggered to sleep or suspend it will invoke the lock script.

```dosini
[Unit]
Description=Lock the screen with i3lock
# Ensure that we run this service before the machine can actually go to sleep
Before=sleep.target

[Service]
User=daylin
Type=forking
Environment=DISPLAY=:0
ExecStart=/home/daylin/bin/lock

[Install]
# Ensure that this is called when we're trying to suspend the machine
WantedBy=suspend.target
```

