---
title: Building faster by parallelizing more
date: 2011-09-01
uuid: urn:uuid:18fdc594-d4ba-11e0-a8fa-782bcb9cb190
aliases:
  - /2011/9/1/Building_faster_by_parallelizing_more.html
---

*tl;dr &mdash; [This patch][patch] may make your builds faster.
[This tool][rse] collects all your build errors and summarizes them after the
build finishes.*

Currently, when you build Firefox with `make -jN`, the build system
parallelizes only within the current directory (*).  So if you build with -j8
and a directory has 9 files, seven of your CPUs will be idle half the time.

About nine months ago, I wrote a patch which adds more parallelism to the
build.  I ran `make` through `strace` and parsed the results to figure out
which top-level directories could be built independently of others.  We haven't
been able to check this in for a variety of reasons (primarily because it's
an awful hack, see [bug 620285][]), but since I'm keeping this patch up-to-date
for myself, I thought I'd share it with others.

Machines with more cores are likely to benefit more from this patch.  A build
on Mounir's 8-core machine went from 11m to 7.5m, a 1.5x improvement.  I saw a
1.2x improvement on my 4-core machine (12m to 10m).

If you want to try the patch out for yourself, you can grab it from [my patch
queue][patch].  I haven't had any problems with randomly-failing builds locally
or on tryserver, although if you have a weird mozconfig, things might not work.

It's easy for error messages to get lost in the scrollback with this patch, so
I wrote a [tool][rse] which intercepts `make`'s output and will report your
build errors to the console after the top-level `make` process quits.  Just put
the script in your `~/bin` and run `rse make`.

The tool works best if you have the `termcolor` package installed.

Of course, the Right Way to increase parallelism in the build is to
[derecursify the build system][bug 623617].  Godspeed, Joey!

_(*) There are a few exceptions, notably within the `content` directory._

[bug 620285]: https://bugzilla.mozilla.org/show_bug.cgi?id=620285
[bug 623617]: https://bugzilla.mozilla.org/show_bug.cgi?id=623617
[patch]: http://hg.mozilla.org/users/jlebar_mozilla.com/patches/raw-file/tip/parallel-builds
[rse]: https://bitbucket.org/jlebar/conf/raw/tip/bin/rse
