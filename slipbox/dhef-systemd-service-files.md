---
title: Systemd Service Files
tags: [linux]
---

Files used to interact with systemd.

There are additional tools on the horizon to replace systemd,
but it has remained standard and likely will for the foreseeable future.

One use case of defining your own systemd file is
to trigger a third-party screen lock based on system events.


I have written a custom "lock" script which wraps i3lock-color.
Without a custom script one could use `/usr/bin/i3lock` as the `ExecStart`.

The below file could be saved at `/etc/systemd/system/i3lock.service`.

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

## Transitioning the above for `NixOS`

In `NixOS` systemd service files can be specified directly in the system
configuration as a nix expression.

The above might be added as follows:

```nix
{
  pkgs,
  ...
}: {
    environment.systemPackages = with pkgs; [
    i3lock-color
    figlet # for ~/bin/lock -> i3lock-color
  ];


  systemd.services.i3lock = {
    wantedBy = ["sleep.target"];
    description = "Lock the screen using a custom lock script";
    before = ["suspend.target"];
    path = with pkgs; [ bash procps figlet i3lock-color];
    serviceConfig = {
      User = "daylin";
      Type = "forking";
      Environment = "DISPLAY=:0";
      ExecStart = "${pkgs.bash}/bin/bash /home/daylin/bin/lock";
      };
  };
}
```

Most of the arguments are straightforward taken from `man systemd.unit`.
One that I think is `nix` specific is the `path` argument which will add
each of the specified packages to the environment of the unit using
`Environment=PATH=/nix/store/path/to...`.

Ideally, my lock script which is managed by `chezmoi` would exist
as an actual package defined in my system configuration
that is itself a wrapper for `figlet` and `i3lock-color`.

