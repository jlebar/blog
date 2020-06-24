---
title: MemShrink process, weeks 97-98
date: 2013-05-08 20:45
uuid: urn:uuid:4a38ae2e-b840-11e2-a458-782bcb9cb190
---

*Nicholas Nethercote is on vacation, so this fortnight's MemShrink report is a
guest post written by [Andrew McCreight][mccr8-twitter].*

## Images

Joe Drew made it so that on B2G [images being displayed on the active page aren't locked](https://bugzilla.mozilla.org/show_bug.cgi?id=862970), allowing them to be discarded when there is memory pressure.  This is important to display image-heavy pages like Pinterest on B2G without OOM crashes.

Andreas Gal [added a preference to control the size of the canvas image cache](https://bugzilla.mozilla.org/show_bug.cgi?id=865929).  The use of canvas with large images was causing OOM crashes for the B2G Gallery app. The limit is set to 10mb for B2G, and remains unlimited on desktop.

## Leak fixes

Scoobidiver noticed a [large increase in empty crashes on Firefox 23](https://bugzilla.mozilla.org/show_bug.cgi?id=866526).  Previously, these have been identified as being caused by leaks of virtual address space.  Scoobidiver and Benjamin Smedberg investigated, found a possible culprit, and saw that the number of empty crashes went down to its previous level, or even lower, after some followup work for that bug was landed.

Timothy Nikkel [fixed a leak](https://bugzilla.mozilla.org/show_bug.cgi?id=864448) caused by some recent changes to reflow-on-zoom.

Justin Lebar investigated a [leak involving long-running automated testing on B2G](https://bugzilla.mozilla.org/show_bug.cgi?id=861492) and determined that it was the [same layers leak previously found and fixed](https://bugzilla.mozilla.org/show_bug.cgi?id=856080), but not backported to B2G18, by new contributor Christophe Mourand.

Randell Jesup fixed a [WebRTC leak](https://bugzilla.mozilla.org/show_bug.cgi?id=862302).

## Miscellaneous

Brian Hackett [reduced the memory usage of IonMonkey compilation](https://bugzilla.mozilla.org/show_bug.cgi?id=804676), which should help on things like JS games that intensively run a lot of JS.

Nicholas Nethercote wrote a patch to [change how decommitted GC arenas are shown in about:memory](https://bugzilla.mozilla.org/show_bug.cgi?id=831588).  Decommitted arenas don't actually use physical memory, so they need to be accounted for differently.

Boris Zbarsky [reduced the memory usage of CSS](https://bugzilla.mozilla.org/show_bug.cgi?id=799816) in certain cases.

[mccr8-twitter]: https://twitter.com/amccreight
