---
title: Why is sorting O(log(n))?
draft: true
---

I want to demonstrate a beautiful connection between two problems you know well:
sorting and binary search.  I'm sure I'm not the first person to think of this,
but I haven't been able to find it written down anywhere.

The inspiration for this connection comes from considering the big-O complexity
of comparison sorts.  Maybe you've seen proofs that mergesort, quicksort, and
heapsort are all O(n log n), and you probably know that no comparison sort can do
better than this. But why is O(n log n) the best one can do?

Here's a leading fact: O(n log n) = O(log n!).  I need to prove this to you, but
maybe you're already suspicious.  Binary search is basically the only
interesting algorithm that runs in logarithmic time, and there are n!
permutations of a list of length n.  Hm...

Intuitively you might expect that n! is O(n^n).  n! is n * (n-1) * (n-2)... and
the first few terms dominate, so that's similar to n * n * n ....  [Sterling's
approximation](https://en.wikipedia.org/wiki/Stirling%27s_approximation), makes
this more concrete it follows from there there that n! is in fact O(n^n).  Take
log of both sides and you arrive at O(log n!) = O(log n^n) = O(n log n).

Now I'll show the connection between sorting and binary search as part of a
proof that comparison sorts can't go faster than O(n log n).

Consider our original, sorted list

  S = [e_1, ..., e_n].

For simplicity, let's assume that all of the elements are unique.  (If this bugs
you, we can easily make them all unique by arbitrarily imposing an order on each
group of equal elements.)

The unsorted list U can be thought of as S permuted according to some
permutation \pi of 1, ..., n:

  U = [e_{\pi_1}, ..., e_{\pi_n}].

Suppose you gave me two of S, U, and \pi.  It'd be easy for me to recover the
third.

 1. Given U and S, I can recover \pi by using a hashtable to figure out which
    elements went where.
 2. Given S and \pi, I can compute U simply by reordering S according to \pi.
 3. Given U and \pi, I can compute S by computing \pi^{-1} and then reordering U
    according to \pi^{-1}.

All three of these take O(n) time.

Below I aim to show that calculating \pi from U using only the tools available
to comparison sorts must take O(n log n) in the worst case.  Before I show you
why this is true, let's consider what would mean if it were true.

First, this would imply that an O(n log n) sorting algorithm exists: Calculate
\pi and then use U and \pi to calculate S (case 3 above).

But less obviously, it would also imply that there is no comparison sort that
can run faster than O(n log n).  Suppose you had a sorting algorithm that ran
faster than O(n log n).  This would yield an algorithm for calculating \pi: Run
this algorithm (yielding S) and then use case 1 above to get \pi.  This
algorithm for calculating \pi runs in less than O(n log n) time, but but by
assumption, it's not possible to calculate \pi faster than O(n log n)!  So
this sorting algorithm must not exist.

So to prove our original claim, that any comparison sort must take O(n log n) in
the worst case, it suffices to show that the fastest algorithm for calculating
\pi from U takes O(n log n) in the worst case.  Let's do it.

Imagine the best algorithm for calculating \pi given U.  At first, there are n!
possible values of \pi; any permutation might be the right one.  Now our
algorithm makes a comparison, asking, does this element appear before this other
element in S?  It gets one bit of information out of this: Yes, or no.  The
absolute best we could do is rule out half of the possible permutations.  Why
only half?  Well, suppose I answered "yes" and you ruled out 75% of the possible
permutations.  Then I could have answered "no" and you'd only have been able to
rule out 25% of the possibilities!  50/50 is the best case if you want to
minimize the worst case.

That, of course, looks a lot like a binary search.

But now we're done; just apply this thinking recursively to each step of the
permutation-finding algorithm and it's clear that if you built an algorithm to
make the worst case run as fast as possible, you'd need to make log_2 n! steps
in the worst case.  QED.
