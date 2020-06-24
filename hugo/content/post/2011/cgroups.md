---
title: Limiting the amount of RAM a program can use
date: 2011-06-15 18:50
uuid: urn:uuid:18b33c00-979c-11e0-be1f-782bcb9cb190
---

Suppose we want to run Firefox but restrict it to using only 50MB of physical
memory.  (Hey, times are tough!)  In operating system terms, we want to limit
Firefox to a 50MB *resident set size* (RSS).  If Firefox tries to use, say,
100MB of memory, half of that will be paged out to disk.

On Linux, `ulimit` is designed to let you do precisely this.  Unfortunately
`ulimit -m` just [doesn't work][ulimit-so] in newer kernels.

I thought that was my last hope, but sfink suggested that no, there is another:
[cgroups][]. I managed to get it to work on my Ubuntu 11.04 machine.  Here's
what I did:

  * Install the `cgroup-bin` package.

  * Edit `/etc/cgconfig.config` and create a group with limited memory.  For
    instance, I added:

        group limited {
          memory {
            memory.limit_in_bytes = 50M;
          }
        }

    The available options are documented [in the kernel sources][memory-kernel]
    and perhaps more readably [by Red Hat][memory-rhel].

    (A public service announcement: If you insert a comment with `#`, the hash
    needs to be at the very beginning of the line.)

  * Re-parse the configuration:

        # restart cgconfig

    If this gives you an error but doesn't explain further, you can view the
    commands it's invoking in `/etc/init/cgconfig.conf`.

  * This should have created a group (a directory) at
    `/sys/fs/cgroup/memory/limited`.  Right now root owns the directory, so you
    have to be root to run programs within the group.  But we don't want to run
    Firefox as root, so let's take ownership of the directory and its contents:

        # chown -R jlebar /sys/fs/cgroup/memory/limited

  * Now we can start Firefox inside this group:

        $ cgexec -g memory:limited dist/bin/firefox

    Load up `about:memory` and go visit some [sites with lots of images][infocus].
    The resident size should stay about the same even as the heap-commited size
    increases.  If all goes well, you'll eventually start paging.

    I noticed that when I set the limit to 50M, Firefox holds steady at an RSS
    of 93M.  I have no idea why that is, but it doesn't really bother me, since
    my goal was cause FF to page, rather than to enforce a particular limit.

You can theoretically move a running process into a group using `cgclassify`,
but it didn't seem to do anything when I tried.  Strangely,
`cgroup/memory/limited/memory.usage_in_bytes` would contain a value within the
desired limit, but `/proc/PID/status` would show an RSS way above the limit.

[cgroups]: http://en.wikipedia.org/wiki/Cgroups
[ulimit-so]: http://stackoverflow.com/questions/3043709/resident-set-size-rss-limit-has-no-effect/3043778#3043778
[memory-rhel]: http://docs.redhat.com/docs/en-US/Red_Hat_Enterprise_Linux/6/html/Resource_Management_Guide/sec-memory.html
[memory-kernel]: http://git.kernel.org/?p=linux/kernel/git/torvalds/linux-2.6.git;a=blob;f=Documentation/cgroups/memory.txt
[infocus]: http://www.theatlantic.com/infocus/
