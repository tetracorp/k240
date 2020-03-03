---
layout: post
title: "Disassembly and analysis tutorial"
categories: data
---

Here I document the process by which I disassemble and analyze the K240
executable. You may find this informative for disassembling other Amiga games,
as well as other games that used the 68000 CPU, notably Atari ST and
Megadrive/Genesis games.

### Disassembly

Disassembly is the process which deconstructs an executable program and turns it
into a series of Assembly-language instructions, which can be analyzed if you
know 68k asm.

The primary tool is a non-interactive disassembler called IRA
([readme](https://ftp.uni-erlangen.de/aminet/dev/asm/ira.readme)
[download](https://ftp.uni-erlangen.de/aminet/dev/asm/ira.readme)).
It is still in active development, and can be compiled to run on Linux (or any
platform with GNU tools), Windows, and MacOSX, with binaries included to run on
AmigaOS 2+, OS4, and MorphOS.

Disassembly with IRA has that issue that it doesn't automatically know what is
executable code and what is data. You first want to run it with the -PREPROC
feature, which guesses the code/data boundaries and generates a config file to
use in future disassemblies.

    ira -A -KEEPZH -NEWSTYLE -COMPAT=bi -PREPROC playk240

However, IRA's guesses are sometimes going to be wrong, so you will need to
manually edit the .cnf file to fix it. All following disassemblies should now
use the config file instead of the preprocessor:

    ira -A -KEEPZH -NEWSTYLE -COMPAT=bi -CONFIG playk240

Determining what is code and what is data requires some technical instinct.
Compare a preprocessed file to a non-preprocessed one. In a preprocessed asm, if
you see a lot of data entries (e.g. `DC.L`) with labels inside them, and hex
numbers which represent common 68k asm instrutions (like `4e75`), that's
probably code misidentified as data. Conversely, in a non-preprocessed asm
(i.e. neither -PREPROC nor -CONFIG), if you see a lot of `DC.L` lines in the
middle of code, or `ORI #0` ($0000 in hex interpreted as an instruction), that's
probably data being misinterpreted as code. Also, `EXT_` declarations often
suggest data misinterpreted as code.

You don't need a perfect disassembly just to analyze and understand the code,
but the closer you can get, the better. It helps if you intend on modifying nad
reassembling the program.

There are some other well-known tools, though I haven't used them for this
project:

- ReSource v6.06 is a commercial interactive disassembler on Amiga from 1994.
  It's no longer updated and hard to get hold of, but a lot of Amiga coders use
  it as their primary disassembler. There is also a
  [ReSource manual](https://stingray.untergrund.net/resource/RESOURCE.pdf).
- [IDA Pro](https://www.hex-rays.com/products/ida/) is a popular interactive
  disassembler which supports many platforms. However, it's commercial, and
  expensive. There's a free version, but it doesn't support 68000.
- [Ghidra](https://ghidra-sre.org/) is an interactive disassembler written by
  the NSA and released to the public in 2019. A third-party add-on called
  [ghidra_amiga_ldr](https://github.com/lab313ru/ghidra_amiga_ldr)
  lets it load Amiga executables.
- [Radare2](https://www.radare.org/r/) is a free and open-source interactive
  disassembler, with a GUI called [Cutter](https://cutter.re/). It supports
  the 68000 CPU, but does not yet have an Amiga hunk file loader.

An advantage of ReSource is that it automatically attempts to identify the type
of variables and such based on how they're referenced, and prefixes it with a
type string.

### Education and reference

Obviously, in order to understand disassembled code, you will need to learn
68000 assembly language, if you don't know it already. Most commercial Amiga
games, including K240, were written directly in 68k assembly rather than a
high-level language like C or AMOS Basic, so there's no meaningful way to
"decompile" such games into a higher level language.

Some useful resources include:

- [68k.hax.com](http://68k.hax.com/), which explains the 68000 instruction set.
- [NVG's 68k docs](https://oldwww.nvg.ntnu.no/amiga/MC680x0_Sections/alphabetical.HTML),
  another 68000 instruction set guide.
- [Mapping the Amiga](https://textfiles.meulie.net/programming/AMIGA/mapamiga.txt),
  a reference to the Amiga system libraries. K240 uses some of these for things
  like file load/save.
- [Amiga Library Docs](https://amigadev.elowar.com/read/ADCD_2.1/Libraries_Manual_guide/node0000.html),
  another library docs
- A [forum thread](https://saltworld.net/forums/topic/12496-unravelling-the-secrets-of-normality-1996/)
  unpacking the MGL compressed data format used by _Normality_, the 1996 MS-DOS
  game Graeme Ing worked on after K240. Might give some clue as to how to unpack
  K240's MGL files.

### Analysis

Making sense of a complex game like K240 is a challenge. Firstly, like most
Amiga games, K240 was originally assembled without debug symbols, meaning that
you have no variable names to work from. There are also no comments to help you.

However, there are a few approaches that can help.

- Try searching for text strings. The `-TEXT=1` option of IRA can help here.
- Try searching for known numbers, or their hexadecimal equivalents. Examples
  include known prices of ships and the starting currency value.
- Many Amiga games used a random number generator seeded from the current
  position of the CRT beam on the screen. Look for references to VHPOSR
  ($DFF006) or perhaps VPOSR ($DFF004). Randomness tends to be used more in
  strategy games and RPGs, so once you identify the random integer generator
  function, you can use that to zero in on code defining the game rules.
- References to the four audio channels AUD0LCH to AUD3LCH ($DFF0A0 to $DFF0D0)
  can identify events which trigger sound, such as hits or damage.
- References to Amiga library calls by OS-compliant games can identify useful
  information, particularly file read/writes in `dos.library`. `JSR (-552,An)`
  is a library open, and with `dos.library`, we can look for a ` JSR` to -30
  (open), -42 (read) and -48 (write). In particular, areas of memory written to
  a save game file usually contain the entire game state.

Once you've identified the purpose of a label, give it a name. Once you've
understood the function of a section of code, you can also add comments.

With IRA, there are two main approaches to this. One way is to simply
find-replace all uses of that label name in the disassembly file (the .asm), and
add comments directly. This is straightforward, but occasionally causes errors,
e.g. when you mistakenly give two labels the same name.

Another way, with the current version of IRA, is to add label names and comments
to the .cnf file, then re-run IRA to add them to the .asm. This helps to avoid
bugs, and allows you to re-disassemble (e.g. to fix code/data boundary errors)
without losing your progress. Label names and comments are added to the .cnf
with the directives SYBOL, COMMENT, and BANNER (see `ira_config.doc`). Other
useful directives include TEXT, JMPB, JMPW, JMPL, and EQU.

### Reassembly

A way to test what parts of the code do is to modify the code and rebuild it
into a working program again.

An ideal tool for this is VASM, an assembler which is still in active
development and will let you compile Amiga executables.

In order to disassemble in a way that VASM will rebuild correctly, the
[IRA readme](https://ftp.uni-erlangen.de/aminet/dev/asm/ira.readme)
suggests first disassembling with the following options:

`-compat=bi`
: Enables two compatibility flags which help ensure correct assembly of programs
originally assembled by certain assemblers.
`-keepzh`
: Keep zero-hunks, i.e. empty sections. K240 doesn't need this but some programs
might use it.

To reassemble, the IRA docs recommend:

    vasmm68k_mot -no-opt -Fhunkexe -nosym -O playk240 playk240.68k.asm

The key here is `-no-opt`, which disables optimizations that might change how
your code is reassembled. The original game executable was probably already
optimized when it was first assembled, so further optimization isn't necessary,
and might actually break stuff.

The `-nosym` option disables debug symbols. If you leave it out, vasm will build
all your label names into the executable, which will make the filesize larger.
However, if you're using the WinUAE debugger to look at code, you actually want
to leave this option out, because you want label names intact.

### Debugging

Another useful tool for understanding Amiga software is the WinUAE debugger,
which will let you step through the program. Hit Shift+F12 to pause the emulator
and load the debugger, then type the command "h" to get a list of commands.
You may need to enable the debugger in options.

Some advice on debugging assembly in WinUAE appears in
[this thread](https://eab.abime.net/showthread.php?t=70007).

You can also export a save state (enable uncompressed save states first) and
analyze or hex edit that.

### Other file analysis

[Maptapper](https://codetapper.com/amiga/maptapper/) is a tool for ripping Amiga
graphics from a memory dump. Configure WinUAE to produce only uncompressed save
states, and ensure your emulated Amiga isn't simulating more RAM than necessary,
so you don't have a lot of space to search.

Maptapper and similar programs like GfxRip are tricky to use, as you must
manually find the sprite boundaries.

Track2File and xdfmaster are handy Amiga programs for unpacking packed files.
Track2File's documentation also describes the formats of certain Amiga games,
which are often an existing format with the four-character leading header
changed to something else to disguise the compression method.
