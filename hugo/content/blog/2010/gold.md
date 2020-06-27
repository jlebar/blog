---
title: gold
date: 2010-03-17
uuid: urn:uuid:53f74dde-9d82-4a33-8c04-97672d32ac26
aliases:
  - /2010/3/17/gold.html
---

Wow, [gold][], Ian Lance Taylor's replacement for the GNU linker ld, is fast.

Firefox builds a large (200mb) shared library called `libxul`, and creating this is often a bottleneck on my machine.  Gold speeds this up significantly:

    $ cd toolkit/library
    $ rm libxul.so
    $ time make
    
    # With ld:
    real    5m21.202s
    user    0m40.499s
    sys     0m50.855s
    
    # With gold:
    real    2m8.786s
    user    0m19.017s
    sys     0m21.341s
This is a 2.5x speedup!

Right now, the only way to get gold is to build binutils from source.  It's not too hard; just download from [here][binutils-download], configure with `--enable-gold`, make, and then either `make install` or add a symlink in your `~/bin` to `binutils-2.20/gold/ld-new`.

Have fun!

[gold]: http://sourceware.org/ml/binutils/2008-03/msg00162.html
[binutils-download]: http://ftp.gnu.org/gnu/binutils/
[high-cpu-instance]: http://aws.amazon.com/ec2/instance-types/
