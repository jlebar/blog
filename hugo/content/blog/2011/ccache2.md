---
title: Set CCACHE_BASEDIR to share object files between trees
date: 2011-04-19
uuid: urn:uuid:ebd366c8-6ab0-11e0-b751-e0f84735e6cc
aliases:
  - /2011/4/19/Set_CCACHE_BASEDIR_to_share_object_files_between_trees.html
---

I [wrote last year][ccache-post] that ccache 3 allows you to share object
files between trees.  It's true, and it's great!  (ccache 3.1 is available in
macports, but Ubuntu 10.10 still has 2.4.  Thankfully it's easy to [build from
source][ccache-source].)

But in my original post, I neglected to mention that in order to make this
work, you need to set the `CCACHE_BASEDIR` environment variable.  ccache uses
this environment variable to determine which paths to rewrite into relative
paths and which paths to leave as absolute.  You just need to set it to some
directory which contains all your source code but doesn't include system
headers; `$HOME` is probably a good bet.

As proof that this actually works, here are my (abbreviated) ccache stats after
clearing my cache and then compiling two identical Firefox trees:

        $ ccache -s
        cache hit (direct)                  3515
        cache hit (preprocessed)             102
        cache miss                          3623
        called for link                       60
        compile failed                        38
        preprocessor error                    20
        files in cache                     10356
        cache size                           1.3 Gbytes
        max cache size                       5.0 Gbytes

We have 3623 cache misses (from the first compile) and 3515 + 102 = 3617 cache
hits (from the second compile).  Not bad!

[ccache-post]: 2010/3/21/ccache_3.0.html
[ccache-source]: http://ccache.samba.org/repo.html
