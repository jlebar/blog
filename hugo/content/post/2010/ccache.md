---
title: ccache 3.0
date: 2010-03-21
draft: false
uuid: urn:uuid:f8e76924-322e-11df-b418-08002769b3d1
---

Along the same lines as my [last post][], [ccache 3.0][ccache] (pre-release,
but hasn't given me any problems) is a big win over previous versions.  In
particular, it can share cached object files between Mozilla tress, no hackery
required.

(Even if you specify all your `-I` directories to gcc using relative paths, the
`-g` argument, which enables debug symbols, causes gcc to emit an absolute path
to the source file in the preprocessed output, presumably so the debugger knows
where to find the source.  Older versions of ccache wouldn't rewrite this
absolute path, and thus would consider two identical files in two different
directories as not matching. So compiling with debug symbols precluded you from
sharing between trees before ccache 3.0.)

Alas, hardlinking with multiple trees still [doesn't work quite right][roc blog].

[last post]: 2010/3/17/gold.html
[ccache]: http://ccache.samba.org/download.html
[roc blog]: http://weblogs.mozillazine.org/roc/archives/2005/01/sharing_binarie.html
