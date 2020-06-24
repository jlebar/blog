---
title: Beware of renice
date: 2013-04-11 20:20
uuid: urn:uuid:e20952ee-a305-11e2-ad4c-782bcb9cb190
---

In B2G, we try to dynamically change processes' CPU priorities depending on how
important we think the process is.  For example, processes in the foreground
get a higher CPU priority.

I spent the past few days tracking down a [bug][] where our mechanism for
changing the CPU priorities didn't seem to be working properly.  Thanks to
[Gabriele Svelto][gsvelto], we figured out today what was going on.

The issue is that the `setpriority` syscall on Linux does not actually set a
process's priority, as you might be led to believe from its man page.  Instead,
`setpriority` changes the priority of a process's *main thread*.  It leaves the
priority of the process's other threads unchanged.  I haven't tested, but from
reading the kernel sources, the `nice` syscall should behave the same way.

Maybe this gotcha is common knowledge, but I was certainly caught unawares.

## Experiment (Linux-only)

Here's a simple demonstration of the issue using [this testcase][gist].  Be
warned that this is a Linux-only test, although it's not hard to fix if you're
intent on trying it on Mac OS.  (Spoiler: renice on Mac OS sets the priority
for all threads in the process.)

    $ cd $(mktemp -d)
     
    $ curl https://gist.github.com/jlebar/5367521/raw/849b6f5c58d054cf10568ac1f3902ab679f9db4f/gistfile1.cpp > test.cpp
    $ g++ -O2 -lpthread -lrt -lm test.c -o test
    $ taskset 1 ./test
    tid 1399: Finished iteration in 1.65s
    tid 1400: Finished iteration in 1.64s

Notice that the two threads are running at the same speed.  Now let's change
the priority.  [`renice` simply calls `setpriority`][renice-source] on the
given pid, so we can use that.

    # In a separate terminal
    $ renice 10 $(pidof test)

    # In the first terminal
    tid 1399: Finished iteration in 8.50s
    tid 1400: Finished iteration in 0.90s

Now notice that the spawned thread (tid 1400) is running almost twice as fast
as it was, while the main process (tid == pid == 1399) is running much slower.

This does not entirely prove my point.  All I've shown so far is that renicing
the main process lowers the priority of the main thread more than it lowers the
priority of the other thread.  But it's still possible that both threads'
priorities were lowered.

This is a simple hypothesis to test: Just spawn a new process that spins the
CPU.  If the spawned thread is actually running with niceness 0, it should
share roughly half of the CPU with the new process.  On the other hand, if
`renice` affected the spawned thread , we'd expect to see the new process get
more than half of the CPU.

    # In a separate terminal
    $ taskset 1 yes > /dev/null

    # In the first terminal
    tid 1399: Finished iteration in 16.95s
    tid 1400: Finished iteration in 1.83s

Thread 1400's time to finish an iteration doubled, from 0.9s to 1.8s,
indicating that it's sharing the CPU equally with `yes`.  So we conclude that
the renice had no effect on the thread.

I tried a similar procedure on my Mac.  Mac doesn't have any way to pin a
process to a CPU, so I launched a bunch of programs each spinning the CPU and
then reniced the main process.  After renicing the two threads contined to run
at the same speed&mdash;just as things should work!

## Conclusions

I take a few lessons away from this.

 * The `setpriority(2)` and `nice(2)` man pages on Linux should mention this
   gotcha.

 * `renice(1)` should probably do the right thing and modify the priority of
   all of the process's threads, or at least it should give you that option.

 * If you're using `setpriority` to modify a thread's priority, you are
   setting its absolute priority on the system, not its priority relative to
   its process's priority.  Therefore you probably want to increase or decrease
   the thread's priority relative to its initial value, instead of setting it
   to an absolute value.

 * It's scary to think about how much of Linux was designed before
   multithreaded programs were common.  You'd never implement things this way
   today.

Gabriele dug up a [thread on LKML][] where it was suggested that `setpriority`
on a pid should modify all threads' priorities, but this was rejected because
the kernel maintainers were afraid this would break userspace programs which
rely on the current behavior.

I'm not so brave as to try to write new functions in glibc that do what we want
here (e.g. modify the priority of all threads relative to the main thread's new
priority), but at least we can fix NSPR.  :)

[bug]: https://bugzilla.mozilla.org/show_bug.cgi?id=847592
[gist]: https://gist.github.com/jlebar/5367521
[renice-source]: http://git.kernel.org/cgit/utils/util-linux/util-linux.git/tree/sys-utils/renice.c?h=stable/v2.13.1#n126
[gsvelto]: https://github.com/gabrielesvelto
[thread on LKML]: https://lkml.org/lkml/2008/9/10/122
