---
title: Git tools for Mozilla
date: 2012-03-18 15:00
uuid: urn:uuid:e4ca99de-7129-11e1-b394-782bcb9cb190
---

I've been working on a [set of git tools][git_tools] for Mozilla, and I'm
pleased to announce them to the community at large.  These tools let you
easily:

  * push from git to a public tree (m-i, m-c, etc.),
  * push from git to try, and
  * export patches to bugzilla.

Have a look at the [readme][] for usage instructions, and of course please file
bugs (or send pull requests) if you encounter any problems.

## Notes

  * I haven't tested on Mac OS, so I don't expect things will work particularly
well there.  Bugs and pull requests are welcome.

  * Pushing from git to hg uses hg qqueues, and will delete the contents of the
git-temp qqueue.  I recommend using a tree for pushing to hg that you don't use
for anything else.  Otherwise, if you push from git to m-i using hg tree X,
then write a patch in tree X, then push again from git to m-i using X, your
patch will be deleted!
  
  (The safe way to re-use hg tree X is to `hg qqueue patches` before writing your
patch.)

  * Most of the credit here is due to bholley, whose tools for pushing from git to
bugzilla and for converting git to hg patches comprise the majority of the
code.

## Why bother?

Git is rather unpopular at Mozilla, so perhaps some justification is in order.
Why bother using git at all?

I decided to try using git a few months ago, because B2G uses a git clone of
mozilla-central, and using both git and hg was painful.  I based my workflow
on [bholley's][bholley].

Although I didn't enjoy learning git, I've come to enjoy using it for hacking
on Firefox.  I particularly like the fact that git branches, unlike mq patches,
are attached to a base revision.

With hg, I'd often end up in a situation where I hack on patch A, qpop it, work
on some other stuff, update my tree, then try to push patch A again.  At this
point, I'd often get conflicts, which I'd have to resolve by hand.  (Otherwise,
I could try to find an old revision atop which the patch applied cleanly, then
`hg rebase` my way to victory.)

This problem simply does not exist with git&mdash;I rebase my branches only
when I intend to.

Also, `git rebase --whitespace=fix` is kind of awesome.

The learning curve is a definite downside&mdash;git's UI is awful&mdash;but now
that I'm up to speed, I have no intention of switching back to hg.

[git_tools]: https://github.com/jlebar/moz-git-tools
[readme]: https://github.com/jlebar/moz-git-tools/blob/master/README.markdown
[bholley]: http://bholley.wordpress.com/2010/10/23/using-git-with-mozilla/
