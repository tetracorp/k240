---
layout: post
title: "About this project"
categories: about
---

_Exploring K240_ is a project to disassemble and analyze the executable and data
files of _K240_, an asteroid mining simulation game released for the Commodore
Amiga in 1994 by Gremlin Graphics.

This project began in 2014, twenty years after the game's original release. Its
primary goal is to discover K240's numerous undocumented game mechanics, many of
which were never revealed to the player despite the game's heavy manual.

This website also serves as a reference site for information on the game in
general, such as its release history.

### Project complete

As of April 2023, the game has been explored and analyzed thoroughly, and all of
the questions have been answered. Thanks to everyone who helped make this
possible. There are still a few unknown variables, but I'm officially marking
the project complete.

### What can we learn?

The biggest questions this project sought to answer:

1. How does ship combat work? (How do ships choose their targets, how
much damage does each weapon deal, and what effect have hardpoints like
Deflector and Warp Generator?)
2. How does ground combat work? (How much damage does each weapon do,
how does fire spread, how many hit points does each building have,
and how does Vortex operate?)
3. How do missiles work? (What is their damage and effect?)
4. How do colonies operate? (What affects population growth, what effect does
radiation have, what effect does population have?)
5. How do buildings work? (What hitpoints do each building have, what
effect does each building have?)
6. How do aliens differ? (What are their tactics and AI routines, do
aliens play by the same rules as Terrans regarding cost and mining,
what are the stats of their ships, missiles and buildings, and how does
each alien differ? Does fire really affect Swixarans more, and why do
abandoned Ore Eater colonies explode?)
7. What are the differences between K240 v1.886 and the bug-fixed version
K240 v2.000?

See the [Frequently Asked Questions](../about/faq.html) list for answers to some
of these, and the rest of the site for answers to all of them.

### How to explore K240?

Various tools aid in analysis of Amiga executables. The most important is Frank
Wille's program
[IRA](http://aminet.net/package/dev/asm/ira),
a modern, non-interactive disassembler which turns an Amiga executable file into
68000 assembly language.

The resulting disassembly is hard to understand, as it's over 40,000 lines of
low-level code with none of the original comments, variable names, or macros.
Some helpful methods to make sense of this include:

1. Searching for known numbers or strings, such as game text or the
known price of a ship. This makes it easy to zero in on code relating
to certain functions.
2. Find-replacing variable names throughout the code and adding comments
once a fuction has been understood. This sometimes makes other parts clearer.
3. Identifying the random number generator function. This is typically
used to "roll dice" or simulate chance, and makes it very easy to zero
in on game rules.
4. Identifying system calls to the AmigaOS functions, particularly
Open(), Read() and Write(). By identifying what parts of memory are
written and read by the save game function, we can tell the entirety
of what holds the current game state. We can also tell how the alien
data files are stored based on how they're read into memory.

Another useful tool is WinUAE, which has a built-in debugger and can
generate uncompressed save states during a game.

Some have recommended ReSource v6.06, an older Amiga interactive disassembler,
though I have not used it for this project.

Most recently I've been using Ghidra. See
[Intro to Amiga reverse-engineering with Ghidra](https://tetracorp.github.io/guide/intro-amiga-ghidra.html)
for an introductory tutorial on this tool.

### Searching for lost resources

I'm also researching various forgotten resources, such as the tutorial VHS tape
and magazine review copies. If you have any old Amiga stuff which may be related
to K240, please respond to one of the Materials Wanted posts on the
[issue tracker](https://github.com/tetracorp/k240/issues/).
