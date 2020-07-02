---
title: Vim search plugin
date: 2011-03-23
id: urn:uuid:5e8f9752-5564-11e0-a95b-001b24dc1e3b
aliases:
  - /2011/3/23/Vim_search_plugin.html
---

*If you're just looking for the `search` plugin, you can get it
[here][search plugin].*

I'm taking a few days off before starting full time at Mozilla next week.  How
better to spend that time than tweaking my Vim configuration?

I may be late to the party, but I just discovered the Vim [Quickfix][] list.
With some tweaking, this is incredibly useful for navigating the Mozilla
source.

(Of course, you can do most of what follows using [MXR][] or [DXR][].  But I
prefer to stay in Vim while I'm coding; I find the context switch to the
browser distracting.  Similarly, you might be tempted to use ctags or cscope to
accomplish these tasks.  But I often find myself searching through IDL, JS, and
even HTML files, which ctags and cscope don't handle.)

## First steps

Suppose you want to look through the references to `nsPIDOMWindow` in IDL
files.  You might run

    :! find . -name '*.idl' | xargs grep nsPIDOMWindow

from inside Vim, or you might hide Vim with ctrl+Z and run the command from
your shell.  If you type this often, you might have a script wrapping it.
Simple enough.

Now suppose you want to open one of the matching files in Vim.  If you have
something like FindMate installed (see [hacking, part 1][]), you need to commit
the filename to memory for a moment, and then type

    :FindMate matching-filename.idl

Now you need to search this file to find "nsPIDOMWindow".  If you decide that
you want to examine one of the other matching files, you either need to
background Vim to look through the output from grep, or run the command again.

This process is pretty annoying if you want to look through 10 or so files,
especially if you do this 10 or so times a day.  There must be a better way.

## Quickfix (almost) to the rescue

Vim's [`:grep`][vimgrep] command gets us most of the way there.  `:grep` will
invoke grep and create a "quickfix list" from the output.  We can then navigate
through matches with `:cn` and `:cp`.  Even better, `:copen` will open a window
with all the results from your last `:grep`; pressing `<enter>` in that buffer
will open the file under the cursor and take you to the matching line.

But to make this work, we need a way to filter by filetype.  We could use
`:vimgrep` and run

    :vimgrep nsPIDOMWindow **/*.idl

but on my machine, this is way too slow.  (Native grep finishes in about a
second, but vimgrep went on for more than a minute before I killed it.)

## Wrapping `:grep`

What we need is a function which wraps `:grep` but lets us invoke something
like the first command in this post, with `find` and `grep`.  Turns out there's
a plugin for this, [ack.vim][], but it uses the grep alternative [ack][].

Unfortunately, ack is about 10 times slower than grep on my machine, so a
search that should take 1s takes 13s instead.  So to get around using ack, I've
written a plugin roughly based on ack.vim which does what I need using find and
grep.  (Thanks to Miles Sterrett for giving me permission to lift the code!)

You can get the plugin [here][search plugin].

I'm sure whatever documentation I write here will be outdated in a week as I
update the plugin, so instead I've included instructions in the plugin itself.
Suffice to say, it solves the problem outlined in this post.  :)

If it works for you (or if it doesn't), let me know!  But be forewarned: In its
current form, the plugin is optimized for browsing Mozilla's source, and isn't
necessarily a general-purpose tool.

[MXR]: http://mxr.mozilla.org
[DXR]: http://dxr.proximity.on.ca/dxr/
[hacking, part 1]: /2010/2/1/Hacking%2C_part_1%3A_Vim.html
[quickfix]: http://vimdoc.sourceforge.net/htmldoc/quickfix.html
[vimgrep]: http://vimdoc.sourceforge.net/htmldoc/quickfix.html#:grep
[ack.vim]: https://github.com/mileszs/ack.vim
[ack]: http://betterthangrep.com/
[search plugin]: http://bitbucket.org/jlebar/search_plugin
