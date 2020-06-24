---
title: "Hacking, part 1: Vim"
date: 2010-02-01 16:55
uuid: urn:uuid:7ba6c41e-1078-11df-a948-08002769b3d1
---

Hello, world!  I thought it would be fitting to begin this blog by talking
about the most basic tool I use: Vim.  I'm a total sucker for tools, and Vim is
one of my favorites.  I don't think I could make much progress hacking at the
Mozilla codebase if it weren't for my [well-shaven][yak shaving] Vim setup.

Let's start with a few vimrc tricks:

 - The wildmenu makes tab completion of filenames nicer.  And it's even nicer
   when you tell Vim not to autocomplete object files.  Add

        set wildmenu
        set wildignore=*.o,*.obj,*.bak,*.exe,*.class,*.swp

   to your vimrc.

 - Vim's syntax highlighting sometimes gets confused when I edit HTML files
   with long Javascript sections (think [Mochitests][]).  You can force Vim to
   re-scan the whole source file with `:syn sync fromstart`.  I have this
   mapped in my vimrc to `,s` as follows:

        noremap ,s :syn sync fromstart<CR>

 - Mozilla doesn't use tabs in their source files, so I force Vim to use
   *spaces instead of tabs* with

        set softtabstop=4
        set shiftwidth=4

   But this creates another problem: Makefiles need to have tabs.  Here's an
   incantation which disables tab expansion in makefiles:

        autocmd FileType make setlocal noexpandtab
        autocmd FileType make setlocal softtabstop=0

In addition, I've found these Vim plugins to be indespensible:

 - [bufexplorer][] is a huge improvement over basic `:ls`, in particular because
   it can order the open files with the most-recently used towards the top.
   This makes the list much easier to scan.

 - [bclose][] adds a `:Bclose` command which closes the active buffer without
   closing its containing window.  I almost always have at least two windows
   open in Vim, and `:bd` will close the window along with the buffer.
   `:Bclose` is a considerable improvement.

 - [spacehi][] highlights trailing whitespace.  Make sure you read the docs to
   learn how to disable highlighting for help files.

 - [findmate][] helps me navigate the labrynth that is Mozilla's directory
   structure.  Rather than type `:e
   browser/components/sessionstore/src/nsSessionStore.js`, I type
   `,,sessionstore.j`, which invokes FindMate to locate any files matching
   `*sessionstore.j*` under the current working directory.

   I modified the script to ignore `.swp` files and directories starting with a
   dot.  Just substitute this for the second line of the FindMate function (as
   one long line, not like it is here):

        let l:list=system("find . \\( -wholename '*/.*' -prune \\) -or 
          \\( -iname '*".l:_name."*' -not -name \"*.swp\" 
          -and -not -name \".*\" -print \\) 
          | sort -d | perl -ne 'print \"$.\\t$_\"'")

That's all I've got for now.  [Stay tuned][rss] for more!

[yak shaving]: http://joi.ito.com/weblog/2005/03/05/yak-shaving.html
[Mochitests]: https://developer.mozilla.org/en/Mochitest
[findmate]: http://snipt.net/voyeg3r/findmate-plugin-for-vim/
[bufexplorer]: http://www.vim.org/scripts/script.php?script_id=42
[bclose]: http://vim.wikia.com/wiki/Deleting_a_buffer_without_closing_the_window
[spacehi]: http://www.vim.org/scripts/script.php?script_id=443
[rss]: feed.atom
