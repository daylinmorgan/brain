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

## Setting up a Windows 11

Installation was originally based on this [blog post](https://bkanuka.com/posts/windows-10-libvirt/),

But as it turns out just using a regular Windows 11 iso solved most of my setup hiccups.

General VM settings:
- Memory: 16384 MiB
- CPUs: 4
- Storage: 80GiB

Under “SATA Disk 1” open the Advanced options and changed Disk bus to VirtIO.
Under “NIC” change device model to virtio.

I downloaded a pre-built iso for win-virtio from following a link in this [repo](https://github.com/virtio-win/virtio-win-pkg-scripts/).
I then used "add hardware" to add this iso to the VM.

I booted up windows and used the win-virtio iso to ensure networking and needed storage drivers were installed.

I also used this [tutorial](https://www.debugpoint.com/kvm-share-folder-windows-guest)
to get file share up and running though.

```nix
virtualisation.libvirtd = {
  enable = true;
  qemu.vhostUserPackages = with pkgs; [ virtiofsd ];
};
```

Perhaps, I can now take this domain and instantiate it using [NixVirt](https://github.com/AshleyYakeley/NixVirt).
Without going into any detail, this worked so now the xml/config for the VM is instantiated with `NixVirt`.

