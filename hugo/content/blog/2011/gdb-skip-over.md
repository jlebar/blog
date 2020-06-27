---
title: Skip uninteresting files and functions in gdb
date: 2011-11-20
uuid: urn:uuid:a555f81c-13e5-11e1-a432-782bcb9cb190
aliases:
  - /2011/11/20/Skip_uninteresting_files_and_functions_in_gdb.html
---

*tl;dr - Build [gdb trunk][], then run `help skip` to be pleasantly surprised.*

After more than a year, I've finally landed a patch to GDB which allows you to
skip uninteresting files and functions while stepping.  In particular, you can
now say "never step into any function in `nsCOMPtr.h`"!

This helps when you're debugging code like the following:

    nsCOMPtr<nsIFoo> foo;
    foo->DoSomething();

Usually, you want to step into `DoSomething()`, but you don't want to step into
`nsCOMPtr`'s `operator ->` function.

With the patch, you can `step` into `nsCOMPtr.h` and then `skip file`.  Now
`nsCOMPtr.h` will be marked as "not for stepping", and you'll always step over
it.

(It's actually a bit more complicated than this: Last time I checked,
`nsCOMPtr.h` is included many times under different names, as `nsCOMPtr.h`,
`../nsCOMPtr.h`, `../../nsCOMPtr.h`, and so on.  GDB sees these each as
separate files, so you have to skip each one individually.  You can work around
this if you put `skip nsCOMPtr.h`, `skip ../nsCOMPtr.h`, etc. in your
`.gdbinit`.  Or you can talk to me about implementing regular expression
matching for skips, which shouldn't be too hard.)

You can also mark a certain function for stepping over with `skip function`.

Skips work like breakpoints; you can enable, disable, and delete them with
`enable/disable/delete skip N`, and you can list them with `info skip`.
Hopefully the documentation in `help skip` is sufficient, but if not, please
let me know.

If you think this feature is interesting, [update to trunk][gdb trunk] (gdb is
easy to build) and let me know how it goes!

*Thanks to the GDB folks who patiently guided my patch through many reviews,
and to Dawson Engler for letting me work on this project while I was in
school!*

[gdb trunk]: http://www.gnu.org/s/gdb/current/
