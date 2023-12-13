---
title: "PGP: Pretty Good Privacy"
tags: [linux, encryption]
---

My main usecase for pgp keys is to get that sweet sweet commit verification.
In the incredibly unlikely attempt someone were to ever try to impersonate my commits they would lack my signature.


Refs: 
- [mike ross](https://mikeross.xyz/create-gpg-key-pair-with-subkeys/)
- [debian wiki](https://wiki.debian.org/Subkeys)

## Securely storing secrets on an offline medium

Use [paperkey](https://www.jabberwocky.com/software/paperkey/)

Take the secret key in key.gpg and generate a text file to-be-printed.txt that contains the secret data:

```
paperkey --secret-key my-secret-key.gpg --output to-be-printed.txt
```

Take the secret key data in my-key-text-file.txt and combine it with my-public-key.gpg to reconstruct my-secret-key.gpg:

```
paperkey --pubring my-public-key.gpg --secrets my-key-text-file.txt --output my-secret-key.gpg
```

If --output is not specified, the output goes to stdout. If --secret-key is not specified, the data is read from stdin so you can do things like:

```
gpg --export-secret-key my-key | paperkey | lpr
```

This way the secret key never exists on disk in a readable format and is instead streamed directly to the print server.
