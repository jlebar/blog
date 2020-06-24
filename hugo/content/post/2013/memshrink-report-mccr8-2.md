---
title: MemShrink process, weeks 98-102
date: 2013-05-31
uuid: urn:uuid:f81eb5ee-ca5e-11e2-9b5a-c82a1426416b
---

*Nicholas Nethercote is on vacation, so this MemShrink report is a
guest post written by [Andrew McCreight][mccr8-twitter].*

## MemShrink process, weeks 98-102

May has been a quiet month for MemShrink, as vacation season begins, but one very important fix landed, as well as the fix of a new leak.

Brian Hackett took advantage of the switch to the Baseline JIT compiler to [delay the analysis of JS scripts](https://bugzilla.mozilla.org/show_bug.cgi?id=865059) until after they have been compiled by the Baseline compiler. This reduces memory usage for scripts that are only run a few times, which is fairly common. On desktop, this reduced startup resident memory by 14mb, which is about 10%. On Fennec, the reduction was 2mb. That 14mb reduction entirely eliminates the difference in memory between startup and 30 seconds later. This was a MemShrink P1.

Andrea Marchesini fixed a [leak involving DOMError and IndexedDB](https://bugzilla.mozilla.org/show_bug.cgi?id=874252) found by Jesse Ruderman.  Fuzzing (automatically generating and running test cases) is an important approach to finding leaks in newly landed code, from situations Firefox developers did not think to test.

[mccr8-twitter]: https://twitter.com/amccreight
