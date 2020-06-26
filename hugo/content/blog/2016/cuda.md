---
draft: true
---

CUDA is a low-level language

## Hardware

Before I can explain the CUDA language, we need to talk about the GPU hardware.

Disclaimer: I'm a software guy.

Let's imagine we're designing a chip for running highly-parallel
computations.  We're after maximum flops here, so we want to cram as many
ALUs and FPUs as possible into our chip.

Our basic game plan is to look at everything big and/or complicated on a
CPU and shrink and/or simplify it.

First to go is the giant last-level cache.  An 18-core Haswell chip might
have 45mb of LLC, using up roughly as much area as all the cores.  Our
top-of-the-line P100 chip has 10% of that, which means more cores for us.

A CPU has both vector and scalar units.  But since we're just interested
in highly-parallel computations, we're going to nix the scalar units
entirely.  Every instruction in our GPU will be SIMD.  While we're at it,
let's make the SIMD lanes large enough to fit 32 floats.  (AVX-512 holds
16).

Modern CPUs have extremely complicated OOO/superscalar pipelines.  And x86
CPUs in particular devote large amounts of die space to instruction decode
and uop execution.  Our GPU cores will have much simpler pipelines and
instruction sets, and not try nearly as hard to do many different ILP
computations in one cycle.  Again, this means: More cores (at a lower
clock speed).

The net result of these changes is that our GPU now fits roughly 100
cores, each with 32 SIMD units.  So that's 3200 floating-point units on
the chip, as compared to maybe 1/20 as many on a super-high-end server
CPU.

But before we go patting ourselves on the back...all we've done so far is
design a really bad CPU.  All of this die area in a modern CPU is devoted
to non-computational tasks for a reason.  The giant LLC and complex
prefetching machinery is there because if every time you do a load you
have to go to main memory, your cores will never get anything done.

Thankfully we have one more trick.  Because we're interested in doing
highly-parallel computations, we can ask our programmers to write their
code in a way that creates many more threads than we have cores.  Then,
you know hyperthreading?  Instead of running two threads simultaneously on
a core, we'll run N of them.  This way when one is blocked on a memory
read, we can just switch to another thread.

We've designed a chip
with a lot of cores, but it's kind of going to suck.  In particular, as
soon as it hits 

If you look at a die shot of a CPU, the first thing you might notice is
the *freaking giant* last-level cache.  (Some Intel chips have 45mb of L3
cache!)  To our eyes, that's space that could be an FPU, so let's shrink
it substantially.  (The new P100 chip from nVidia has only 4mb LLC.)

- Reduce cache 

If we look at a modern server-class CPU, the first thing we might notice
is the giant last-level cache.  An 18 core Haswell chip has 45mb of cache,
using a huge amount of die area. 
