---
title: Faster and smaller clones of branches
date: 2011-05-20
uuid: urn:uuid:6148efe2-8319-11e0-87cd-e0f84735e6cc
---

We're moving towards a world with increasingly many branches.  Pulling a full
clone over the network can take some time, but if you already have a local
clone (say of mozilla-central), you can do a lot better.

With thanks to the Mercurial developers who
[pointed this trick out to me][hg bug], here's how.

## Pulling using an existing clone

Suppose we want to clone the cedar branch.  First, make a copy of your
mozilla-central clone:

    ~$ hg clone ~/mozilla-central cedar

Now modify the cedar tree's default path, so `hg pull` pulls from the cedar
repo rather than from `~/mozilla-central`.  Open `~/cedar/.hg/hgrc` with your
favorite text editor and change it to:

    [paths]
    default=http://hg.mozilla.org/projects/cedar

Next, we need to remove the commits from your mozilla-central clone which
aren't present in the upstream cedar repository:

    ~/cedar$ hg strip --no-backup 'roots(outgoing())'

Now we can pull from cedar and we should have an up-to-date clone:

    ~/cedar$ hg pull -u

In addition to being faster, this process has another advantage over cloning
cedar directly: It allows hg to [share storage][hardlink] between your
mozilla-central and cedar repositories.

(Note: This process doesn't work so well with some repositories &mdash; I think
it works better with branches which haven't been around for too long.  For
instance, the `hg strip` step took upwards of 20 minutes when I ran it on the
tracemonkey branch.)

## hg relink

If you already have two related trees and you want to share storage between
them, just use the [relink][] command.  Enable it in your hgrc:

    [extensions]
    relink =

and then run

    ~/cedar$ hg relink ~/mozilla-central

This saves about 400MB per 1.1GB checkout on my machine:

    ~$ du -hs ~/cedar
    1.1G ~/cedar

    ~$ du -hs ~/cedar ~/mozilla-central
    1.1G ~/mozilla-central
    681M ~/cedar

[relink]: http://mercurial.selenic.com/wiki/RelinkExtension
[hardlink]: http://mercurial.selenic.com/wiki/HardlinkedClones
[hg bug]: http://mercurial.selenic.com/bts/issue2818
