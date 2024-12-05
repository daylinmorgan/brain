---
title: Libvirt
tags:
- linux
- dev
- devlog
---

This is a devlog about getting libvirt up and running on NixOS to use Windows.

I started getting odd errors from VirtualBox related to KVM modules loaded by the kernel.
This motivated me to evaluate `libvirt` as an option for running virtual machines.

My primary need is having quick access to windows only software, primarily for work purposes.
This means I need the setup to be reliable, performant and easy to access.
Currently, I have a Windows 10 VM managed by VirtualBox and so long as it starts I have no issues with it.

To get started, I headed over to the official wiki for nixos and looked at the `libvirt` [page](https://wiki.nixos.org/wiki/Libvirt). 
And added the below snippet to `hosts/othalan/virt.nix`. If this works well, I'll abstract the config to a nixosModule.

```nix
{
  pkgs,
  enabled,
  ...
}:
{
  programs.virt-manager = enabled;

  virtualisation.libvirtd = enabled // {

    # Enable TPM emulation (optional)
    libvirtd.qemu = {
      swtpn = enabled;
      ovmf.packages = [ pkgs.OVMFFull.fd ];
    };

    # Enable USB redirection (optional)
    spiceUSBRedirection = enabled;
  };

  users.users.daylin = {
    extraGroups = [ "libvirtd" ];
  };
}
```
[ref](http://bkanuka.com/posts/windows-10-libvirt/)
