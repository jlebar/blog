---
title: "PSA: hg inotify extension"
date: 2011-08-10
id: urn:uuid:26ded498-c306-11e0-8fd2-782bcb9cb190
aliases:
  - /2011/8/10/PSA:_hg_inotify_extension.html
---

*tl;dr &mdash; Enable the hg `inotify` extension to make hg faster.*

People often complain on #developers that Mercurial is slow compared to Git.
But if you run Linux, you may be able to make hg much faster by enabling the
`inotify` extension.  (You know the drill: Add `inotify=` under `[extensions]`
in your `~/.hgrc`.)

The Mercurial wiki ominously warns that this extension is
"[definitely considered experimental][inotify-wiki]", whatever that means.
I've been using inotify for a few weeks now without any problems.  (I regularly
back up my patch queue to a Mozilla user repository, so as to limit the
possible damage if something goes kaboom.)

And man, is it *fast*.

[inotify-wiki]: http://mercurial.selenic.com/wiki/InotifyExtension
