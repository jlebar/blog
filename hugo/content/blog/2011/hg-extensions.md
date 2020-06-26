---
title: hg tips
date: 2011-01-14
uuid: urn:uuid:0303107c-2039-11e0-a733-0015c5683ca0
---

Since this [appears][zpao-1] [to be][zpao-2] in fashion, I thought I'd share a
few mercurial tips of my own.

## qstatus

I created a `hg qstatus` command by adding the following to my hgrc:

    [extensions]
    parentrevspec =

    [alias]
    qstatus = status --rev qtip^:qtip

This shows the files modified by your topmost mq patch.

I often switch to a patch and then run

    $ vim `hg qst -n`

to open all the files touched by that patch.

## Indexing into your patch queue

Passing `-v` to `hg qseries` shows you which patches in your series are applied
and gives a zero-based index for each patch in your queue.  For instance,

    $ hg qseries -v
    0 A foo
    1 U bar
    2 U baz

This is particularly useful because mq operations can take these indices as
operands, as in

    $ hg qgoto 2
    applying bar
    applying baz
    now at: baz

You can make `-v` the default for `qseries` and `qapplied` by adding this to
your hgrc:

    [defaults]
    qseries = -v
    qapplied = -v

I like combining this with [hg-prompt][]; there's now a `patch|topindex`
command in hg-prompt which corresponds to the index of the topmost applied
patch in your queue.  (It's in the main repository, but the docs aren't yet
updated.)

[zpao-1]: http://blog.zpao.com/post/2690265795/hg-prompt-makes-my-eyes-happier
[zpao-2]: http://blog.zpao.com/post/2749865516/use-a-pager-with-mercurial
[hg-prompt]: http://sjl.bitbucket.org/hg-prompt
