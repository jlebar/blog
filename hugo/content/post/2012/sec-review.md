---
title: Security Review Form Helper
date: 2012-04-27
uuid: urn:uuid:d542fdde-9088-11e1-9283-782bcb9cb190
---

I learned about our new security review form yesterday.  Developers are expected to respond to [eleven questions][questions] for each bug that has a security review.

I dislike filling in forms, so I wrote a [tool to answer most of these automatically][tool].

Just put the bug number in the query string, then fill in the last question and add any additional points of contact to the first question.  Most of the answers are hard-coded, but they should be correct for the vast majority of changes to Firefox.

[questions]: https://bugzilla.mozilla.org/show_bug.cgi?id=749376#c0
[tool]: http://people.mozilla.org/~jlebar/tools/sec-review.html?697132
