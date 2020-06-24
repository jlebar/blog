---
title: Boolean parameters to API functions considered harmful.
date: 2011-12-16 17:10
uuid: urn:uuid:86af85e8-2832-11e1-92fc-782bcb9cb190
---

Can you spot the [bug][hive-bug] in the following code?

    _xhr.open(options.type, options.url, options.sync); 

The problem is that the last param to xhr.open is whether the xhr is *async*.
Ouch.

Turns out, this code was written intentionally, and used browser sniffing so it
only failed on Gecko.  It appears that the author believed that Gecko's
sync/async argument went in the opposite direction as WebKit's (maybe this was
true at some point in the past?).  This has been [fixed][hive-fix] as of a few
hours ago, but it seems that the code was broken on Gecko for two years.

As further illustration, what does the boolean parameter here mean?

    nsCOMPtr<nsIObserver> observer = ...;
    mDocument->AddObserver(observer, "load", true);

Even if you're familiar with this interface, and you know that the first
boolean parameter has to do with strong vs. weak references, do you remember
whether `true` means strong or weak?  I never can, because there's no obvious
way to map from true/false to strong/weak -- it's arbitrary, just as the
true/fase to sync/async mapping is arbitrary.

*(In case it's not clear, boolean parameters are perfectly fine when the
parameter really is a boolean.  For example, nobody will be confused by
`setVisiblity(false);`.)*

We can do better than this.

When you have an API which takes a boolean parameter which chooses between two
behaviors, just make two API functions, and put the behavior in the function
name!  See how much clearer these APIs become if we do this?

    xhr.openAsync(options.type, options.url)
    mDocument.AddWeakObserver(observer, "load");

We should demand clear APIs, both from ourselves and, where we can, from
others.  **Functions are cheap, but bugs are not.**

[hive-bug]: http://code.google.com/p/thermetics-forum-extensions/issues/detail?id=33
[hive-fix]: https://github.com/rwldrn/jquery-hive/commit/a21994a66e4e8f13811f0a54783cbd235b5f17f2
