---
title: Replacing Bash
date: 2010-02-01
id: urn:uuid:7baf959e-1078-11df-a948-08002769b3d1
aliases:
  - /2010/2/1/Replacing_Bash.html
---

I've been thinking lately about replacing Bash as a scripting language.  To be
clear: I use Bash as my interactive shell, and I'm generally pleased with it.
Here I'm concerned only with Bash as an interpreter of scripts saved to a file.

To illustrate with an example, can you figure out what these two lines of Bash
do?

    a = 1
    if [$b == "" -a $a == 1]; then ...

This looks pretty simple, but did you notice all the bugs?

 - `a = 1` is invalid; it needs to be `a=1`, otherwise Bash will try to run a program called `a`.
 - There need to be spaces on either side of the square brackets.
 - `$b == ""` won't work unless we use double brackets, since `b` is undefined.
 - `-a` doesn't work with double brackets.

Got all that?  Here's what I should have written:

    a=1
    if [[ $b == "" && $a == 1 ]]; then ...

Unless you really know what you're doing, spending 10 minutes trying to do
something like this in Bash is a recipe for at least a few new gray hairs.  It
really makes you appreciate the beautiful syntax of languages like Python.

Bash's syntax isn't entirely unusable.  In fact, I'd argue that in a lot of
cases, you can create really elegant scripts in Bash.  Consider the following
problem:

> Some text files (all with the extension `.idl`) beneath the current
> working directory contain UUID declarations of the form "uuid(xxx)".  Print out
> the files which share a UUID with at least one other file.

Here's how I implemented this in Bash:

    #!/bin/bash
    DUPES=$(find . -name '*.idl' | xargs grep -oh 'uuid(.*)' | sort -f | uniq --repeated)
    for dupe in $DUPES; do
      find . -name '*.idl' | xargs fgrep -n $dupe
      echo '---'
    done

This isn't perfect.  My problem statement suggests that a UUID has to be
duplicated in two different files in order to be flagged, but this script
ignores that restriction.  It also searches all the files once for each
duplicate, although this isn't such a big deal since I don't expect there to
be many duplicates.  Last, the command options are somewhat obtuse.  What's
`grep -oh` do?  But that's mostly my fault for not using long-form arguments
(`grep --only-matching --no-filename`).  My point is that this is serviceable.

Compare the Bash script with a native Python implementation:

    #!/usr/bin/python3
    import os, re, fileinput

    idls = []
    for root, dirs, files in os.walk("."):
      for f in files:
        if f.endswith(".idl"):
          idls.append(os.path.join(root, f))

    uuids = {}
    pattern = re.compile("uuid\(.*\)")
    input = fileinput.input(idls)
    for line in input:
      id = pattern.search(line)
      if not id:
        continue
      uuid = id.group(0)
      if uuid not in uuids:
        uuids[uuid] = []
      uuids[uuid].append(input.filename())

    print ([(uuid, files) for (uuid, files) in uuids.items() if len(files) > 1])

Although this has the advantage of doing exactly what I wanted (it won't flag a
UUID which is duplicated only within one file), the Bash script still clearly
wins by virtue of being so much simpler.

I'm not an expert Bash or Python coder.  A Bash expert wouldn't have so much
trouble with if statements, and a Python expert could probably write a simpler
script.  But *I don't want to be an expert*; I'm just writing a script to get
something done.  Which brings me to the point of all this:

**I want a scripting language which combines the power of find, grep, and pipes
with the clean, easy-to-learn syntax of Python.**

I know I'm not the first person to ask for this.  Here are just a few projects
with similar goals:

 - [Windows PowerShell][] and its open-source clone, [Pash][]
 - [IPython][]
 - [Hotwire][] (also [here][Hotwire2])
 - [rush][]

[Windows PowerShell]: http://technet.microsoft.com/en-us/scriptcenter/dd742419.aspx
[Pash]: http://pash.sourceforge.net/
[rush]: http://rush.heroku.com/
[Hotwire]: http://code.google.com/p/hotwire-shell/ 
[Hotwire2]: http://cdn.hotwire-shell.org/index.html
[IPython]: http://ipython.scipy.org

These might be an improvement over Bash, but I'm not entirely pleased with any
of them, for a variety of reasons.  I'll explain why in a forthcoming post.
