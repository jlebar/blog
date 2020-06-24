---
title: Replacing Bash, part 2
date: 2010-02-03
uuid: urn:uuid:b189712a-113c-11df-a9d6-08002769b3d1
---

In my [last post][], I talked about why I want to replace Bash as an
interpreter of scripts.  In brief, although Bash (combined with pipes, find,
grep, and the like) is well-suited to interactive use and some scripting tasks,
it fails miserably at general-purpose programming tasks one often wants to
integrate into more complicated scripts, like conditionals.

Today I want to talk at a high level about the properties I think a scripting
language needs in order to be a viable replacement for Bash.  I'll dive deeper
into these ideas later.  Because it doesn't have a name yet, let's just call
the language B' (B-prime).

B' must be **ridiculously easy to learn**.  Shell scripts are tools.  I don't
want B' to try and teach me an entirely new paradigm for writing code.  I just
want to write my script quickly and be done.

B' must be **trivial to distribute and install**.  Most important scripts don't
live forever on a single computer, so it's important that it's easy to run a B'
script on any machine.  Ideally, you could distribute along with your B' script
a magic file which would contain everything you'd need to run the script.

B' must be **obviously better than the alternative**.  Bash has a lot of
momentum behind it.  If anyone is to invest in something new, it needs to be
obviously better.  This is as much about design decisions as it is about
documentation and marketing.

Does B' already exist in some form?  Maybe.  [Hotwire][] is strongly focused on
interactive use, so it's not terribly useful to me.  It [doesn't have
conditionals or loops][hotwire no loops], for instance.  [IPython][] and is focused on replacing
Python's interactive shell, not on performing shell-script-like tasks.

[fish][] looks more sane than most shells, but it's still a shell rather than a
general-purpose programming language which is good at shell-like tasks, so
you're still stuck with [using `bc` to do math][fish math].  No thanks.

[rush][] is the best candidate I've read about so far.  It elegantly integrates
find and grep into Ruby.  Unfortunately, it doesn't have strong facilities for
interacting with external programs; it has a "run this string in Bash" function
instead.

The Hotwire wiki has a long [list][similar projects] of similar projects.
People want B'.  But I'm not sure it exists just yet.

[last post]: 2010/2/1/Replacing_Bash.html
[rush]: http://rush.heroku.com/
[Hotwire]: http://code.google.com/p/hotwire-shell/
[Hotwire no loops]: http://code.google.com/p/hotwire-shell/wiki/HotwireScripting
[IPython]: http://ipython.scipy.org/
[fish]: http://fishshell.org/
[fish math]: http://fishshell.org/user_doc/commands.html#math
[similar projects]: http://code.google.com/p/hotwire-shell/wiki/RelatedProjectsAndIdeas
