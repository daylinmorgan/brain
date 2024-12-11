---
title: SOPS
tags:
  - dev
  - nixos
  - devlog
---

This is a devlog of how I initially started using SOPS and sops-nix to improve my workflow with NixOS.

Some examples of thing's I'd like manage within my config:

- restic password files
- mullvad vpn password file
- attic key file

Before I started handling keys and secrets I went ahead and install `sops-nix` using flakes and the included `nixosModule`.

I added the module (while refactoring my generator) and that didn't seem to install sops.
So, I also added the sops package from `nixpkgs` for `othalan`.

I've decided to use `ssh-to-age` to generate my `age` keys for use with `sops`.
I ran this command to generate an `age` key for my user:

```sh
nix-shell -p ssh-to-age --run 'ssh-to-age < ~/.ssh/id_ed25519.pub'
```
I could have used a [`gpg`](./hvxi-pgp-signing-keys.md) key but this seemed easier.
I added this to `.sops.yaml` in the base of the `oizys` repo.

After I saved the file and tried to open it again I was met with an error about my key not working.

```sh
sudo ssh-keygen -t ed25519 -f /etc/ssh/ssh_host_ed25519_key
nix-shell -p ssh-to-age --run 'sudo cat /etc/ssh/ssh_host_ed25519_key.pub | ssh-to-age'
```

This was resulting in errors. I think the issue is that age keys needed to have been written to a file that sops is looking at.
I remedied this by running the following.

```sh
nix run 'nixpkgs#ssh-to-age' -- -private-key -i ~/.ssh/id_ed25519 > ~/.config/sops/age/keys.txt
```
Now when I ran `sops hosts/othalan/secrets.yaml` it worked...I had no idea this was necessary, but then again I'm not familiar with `age`.

Next I started by adding a secret to access my `restic` backup repository.

Importantly, I also added this line to my configuration:

```sh
sops.age.sshKeyPaths = [ "/etc/ssh/ssh_host_ed25519_key" ];
```
which then resulted in this output when building:

```text
sops-install-secrets: Imported /etc/ssh/ssh_host_ed25519_key as age key with fingerprint age1t4k04mjltmmhljnwugm6y4dejtu72vv4fd4anxxfsdpkapfnfauqe765gy
```

Which I assume is how the secrets will be activated.
After rebuilding, the file I wanted to exist was as expected at `/run/secrets/restic-othalan`.
But I need to use `sudo` to verify this.
This file will need to be accessible to my user `daylin`.

I adapted the instructions from the `sops-nix` README and added the following to make the secret accessible:

```nix
sops.secrets.restic-othalan = {
  # Permission modes are in octal representation (same as chmod),
  mode = "0440";
  # It is recommended to get the group/name name from
  # `config.users.users.<?name>.{name,group}` to avoid misconfiguration
  owner = config.users.users.daylin.name;
  group = config.users.users.daylin.group;
};

```

With this, I now am able to access my `restic` password without needing to setup the file myself.
So long as I can prove myself to `sops` of course.
