---
title: Programmatic control of the perf profiler from Firefox
date: 2012-04-24 22:20
uuid: urn:uuid:ec5209ac-8e7b-11e1-b047-782bcb9cb190
---

One of the killer features of profiling on the Mac was that you could programmatically start and stop the profiler.

I say "was" and "could" because the CHUD interface we used for this was removed in MacOS 10.7.  There may be some way to make this work in the brave new world of Instruments, but as of now, it doesn't.

I don't have a solution for those of us running Lion, but I do have a solution for those of us running Linux.  After much help from sfink, I landed [bug 741652][] today.  This lets you programmatically start and stop Linux's [perf][] profiler.

In your code, add:

    JS_StartProfiling("this-value-is-ignored");
    // Do some stuff you want to profile
    JS_StopProfiling("this-value-is-ignored");

Then run Firefox with the `MOZ_PROFILE_WITH_PERF` environment variable defined.  (You'll probably want to add `ac_add_options --enable-optimize --enable-profiling` to your mozconfig.)  Finally, view the results with

    $ perf report -i mozperf.data

You can set custom `perf record` flags with the `MOZ_PROFILE_PERF_FLAGS` environment variable.  By default, we pass `--call-graph`.  (Pro tip: Try passing `--stat`.  It collects information about which thread did what, letting you filter out noise from other threads which might creep into your profile.)

You can use `MOZ_PROFILE_PERF_FLAGS` to profile something other than CPU time, but at least on my kernel, perf seems to have a bug which causes it to hang when sampling some of the more exotic counters.  Killing perf when it's hung corrupts its data file, so there's not much we can do to work around this.  The current patch hangs Firefox when perf is hung, so you'll at least notice.  :)

One last thing: Versions of perf newer than 3.0 seem to have much better error messages.  It's ridiculously easy to build a new version of perf, so if you're running to mysterious problems, I recommend you try the newer version.  Download the [kernel source][], cd tools/perf, make (and install the packages it prompts you to install), and make install.  (It'll install itself into your `~/bin`.)  I'm running the 3.0 kernel with perf from the 3.3 kernel without difficulties (save the hangs with exotic events I mentioned earlier, but I think those are unrelated).

Happy profiling!

[bug 741652]: https://bugzilla.mozilla.org/show_bug.cgi?id=741652
[perf]: https://perf.wiki.kernel.org/
[kernel source]: http://kernel.org/
