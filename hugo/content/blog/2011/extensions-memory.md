---
title: "The carrot, the stick, and the wrench: Add-on leaks are everyone's problem."
date: 2011-11-13
id: urn:uuid:fb6ba78a-0e70-11e1-be7f-782bcb9cb190
aliases:
  - /2011/11/13/The_carrot,_the_stick,_and_the_wrench:_Add-on_leaks_are_everyone's_problem..html
---

We've made a lot of progress with MemShrink in just a few months.  There's
plenty more work to do, but at this point, the vast majority of bugs which take
the form of "OMG Firefox is using 8 zettabytes of RAM" are not due to problems
in Firefox.  Instead, **most major memory bugs are due to problems in Firefox
add-ons.**

We in MemShrink have generally argued that bugs caused by add-ons aren't
something we can fix, so fixing them can't be a priority.  We've reached out to
the developers of the leaky add-ons we've been made aware of, and we've
discussed strategies to automatically fix certain classes of add-on leaks.  But
the first approach doesn't scale, and the second approach is Very Hard and
unlikely to happen.

**No add-on is immune from the risk of leaking.**  Even the venerable Adblock
Plus, the most popular add-on on AMO and by all measures a well-written add-on,
suffers from a [compartment leak][abp-leak].

Given that add-ons are so frequently fingered as the causes of leaks, and given
that so many add-ons leak, my thesis is that we should stop using the fact
that we don't control add-ons' code as an excuse not to try to fix this
situation.

The fact is, **if we take credit for our vibrant add-on community, we must take
responsibility for the problems those add-ons cause.** This shouldn't be
controversial; we already check to ensure that add-ons aren't outright
malicious before posting them to AMO, acknowledging that the buck stops at
Mozilla when there's a misbehaving add-on.  Even if it's not our bug, it's in
our software, and people will [blame us, not their add-ons][blame us].

So what can we do to fix this?  I suggest a three-pronged approach, consisting
of the carrot, the stick, and the wrench:

  * **The carrot**, aka [bug 695471][]
  
    As part of the process of submitting an add-on to AMO, we should ask the
    submitter to check for zombie compartments.  These are easy to check for,
    and many kinds of memory leaks manifest themselves as zombie compartments.

    This bug is assigned, and I hope we can get it pushed through soon.  It's a
    P1 MemShrink bug, so we'll be watching it closely.

  * **The stick**, aka [bug 695481][]
  
    The carrot helps us with new add-ons, but it doesn't address leaks in
    extant add-ons, whose authors won't have seen the advisory prompt.  It also
    doesn't help us with careless add-on developers.
    [The economist in me][economist] thinks **what we really need is an
    incentive for add-on developers to fix their code.**

    From another perspective, add-ons are all about empowering our users.  But
    it's not particularly empowering to install an add-on blind to the
    performance or memory problems it causes.  We have the capability to inform
    users of a problem before they install an add-on, and we should.

    Thus I suggest we call out add-ons with outstanding bugs on the add-on
    download page.  Let users give informed consent before installing an add-on
    with known memory or performance bugs.  (Maybe we could even indicate which
    add-ons are known to leak in about:addons, so users with memory or
    performance problems can try disabling the known-buggy addons.)

    I understand that any kind of wall-of-shame on AMO is a touchy subject.
    Wladimir Palant, the developer of Adblock Plus, wrote an excellent
    [series][abp-blog] about the problems with AMO's "slowest addons" testing,
    but I think the main lesson to be learned is that **we should give add-on
    developers a chance to respond to what amounts to an allegation on our part
    before announcing it on AMO.**  We should treat add-on developers as
    partners because, like it or not, their code runs inside our product --
    they *are* our partners!

    This is a MemShrink P2 bug and is currently unassigned.  I'd love to work
    with someone from the AMO team to make this a reality.

  * **The wrench** (used as a tool, not a bludgeon!)
  
    Last, we need to improve the tools add-on developers can use to track down
    leaks.  Right now, it's hard to determine why a compartment is alive.  But
    this kind of debugging needs to be easy if we expect all add-on developers
    to do it.

    [bug 695348][] is a start (and an assigned MemShrink P1), but we'll
    probably need other tools like it.

It's time for us to stop saying there's nothing we can do to fix problems
caused by add-ons.  We can give developers the tools they need to solve leaks,
we can give them the incentives to fix those leaks, and we can empower users so
they know what they're getting themselves into when they install an add-on.

People love their add-ons, and we need to ensure that running Firefox plus a
few popular add-ons is as awesome an experience as running Firefox with no
add-ons.

[abp-leak]: https://bugzilla.mozilla.org/show_bug.cgi?id=672111
[blame us]: http://i.imgur.com/Ftxty.jpg
[bug 695471]: https://bugzilla.mozilla.org/show_bug.cgi?id=695471
[bug 695481]: https://bugzilla.mozilla.org/show_bug.cgi?id=695481
[abp-blog]: http://adblockplus.org/blog/overview-for-mozilla-s-add-on-performance-measurements
[bug 695348]: https://bugzilla.mozilla.org/show_bug.cgi?id=695348
[economist]: http://www.youtube.com/watch?v=VVp8UGjECt4
