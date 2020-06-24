---
title: "Use MOZ_QUIET environment variable to disable DOCSHELL/DOMWINDOW printfs."
date: 2011-08-04
uuid: urn:uuid:83186b24-beb1-11e0-9448-782bcb9cb190
---

I just landed [bug 673252][] on mozilla-inbound.  This lets you disable those
annoying `+++DOMWINDOW` and `+++DOCSHELL` printfs by defining `MOZ_QUIET` in
your environment.

To be concrete, you just need to run:

    $ MOZ_QUIET=1 dist/bin/firefox

or alternatively put

    export MOZ_QUIET=1

in your `~/.bashrc`.

[bug 673252]: https://bugzilla.mozilla.org/show_bug.cgi?id=673252
