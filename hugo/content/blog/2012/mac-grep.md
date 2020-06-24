---
title: GNU grep is 10x faster than Mac grep
date: 2012-11-28
uuid: urn:uuid:53d569de-391c-11e2-8a9e-c82a1426416b
---

If you're on a Mac and you ever use grep, do yourself a favor and do

    $ port install grep

That's likely all you need to do to install and make default GNU grep, which on
my machine is a ~10x speedup over the grep that ships with Mac OS.

To wit, here are some benchmarks on my [git clone of mozilla-central][git-m-c],
with a warm disk cache.

Before:

    mozilla-central$ which grep
    /usr/bin/grep
    mozilla-central$ time git ls-files -z | xargs -0 grep foobar > /dev/null
    real 0m19.583s
    user 0m18.853s
    sys  0m0.722s

After:

    mozilla-central$ which grep
    /opt/local/bin/grep
    mozilla-central$ time git ls-files -z | xargs -0 grep foobar > /dev/null
    real 0m1.386s
    user 0m0.754s
    sys  0m0.613s

Of course in this particular case I could use `git grep`, which doesn't use the
system's grep.  It's about the same speed as GNU grep:

    mozilla-central$ time git grep 'foobar' > /dev/null
    real 0m1.470s
    user 0m0.956s
    sys  0m1.845s

`/usr/bin/grep -V` says that it's FreeBSD grep version 2.5.1.  I don't know if
the grep FreeBSD actually ships is similarly slow.

[git-m-c]: https://github.com/mozilla/mozilla-central/
