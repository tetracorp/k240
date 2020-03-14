---
layout: post
title: "Differences between versions"
categories: history
---

K240 was released in two main versions: v1.886, with a build date of 20 May
1994; and v2.000, build date 7 June 1994. You can press "V" during play to find out
which version you have. I believe v2.000 was a
[bugfix](../game-mechanics/bugs.html) patch.

Additionally, a demo version of K240 was given away with CU Amiga issue #77 (Mar
1994) as a coverdisk. There are some differences; notably some bugs, and
different sprites for certain buildings. I intend to disassemble this for
comparison eventually. I don't know whether or not any other magazines had a
K240 coverdisk.

There are also various cracked pirate releases, but aside from removed
copy-protection and cracktro, these seem to be largely unchanged.

1. Table of Contents
{:toc}

### Main game executable differences

The following differences apply between the v1.886 and v2.000 versions of the
main `playk240` executable file.

#### Fleet bug fix

The main game executable `playk240` appears to have only one functional change
between the v1.886 and v2.000 release, which is a single additional line of code
to address a major [bug](../game-mechanics/bugs.html) that crashes the game
when handling fleets.

At address 0xc0d8 in v2.000 (0xc0da in v1.886), at the end of a loop, it checks
the value in (6,A0), leaving the loop on a negative value; otherwise, it loads a
new value into (6,A0) and repeats the loop. In v2.000, it an extra `BNE.W`
instruction is inserted at 0xc0de between the `BMI.S` and `MOVE.L`, which
repeats the loop without updating (6,A0) if it is equal to a non-zero value.
This extra four-byte instruction increases all addresses after 0xc0de in the
executable by 2.

#### Version strings

The version string at 0x6016 in both versions is also updated. This can be seen
in-game by pressing the `V` key. The two version strings are:

    K240 - VERSION 1.886,  20-5-94 13:25
    CLICK MOUSE TO CONTINUE GAME...

    K240 - VERSION 2.000,  7-6-94 11:15
    CLICK MOUSE TO CONTINUE GAME...

The v2.000 version string is two bytes shorter overall.

#### Padding

At the very end of the first hunk, after the cheats, the v2.000 disassembly has
an additional two bytes, `0xb900`. This is never called by the program and is
probably just padding to align the next section.

Overall, v2.000 gains four bytes from the fleet fix and two from the padding,
but loses two from the shorter version string. The result is that v2.000 is four
bytes larger overall.

### Cracked version vs original

The authorized free distribution of K240 comes from a cracked pirate version
which has a single two-byte change allowing any authorisation code to work.

At 0x40c6 in the v1.886 disassembly we can see where the manual protection check
has been skipped by simply branching to the next label. The original
instruction, `MOVE.W #$025c,D0`, in hexadecimal as `303c025c`, has simply had
its first two bytes overwritten with `6016`, which branches forward 24 bytes as
if the correct code had been entered.

Incidentally, the variable 0x25c is the ID number of the game string
"AUTHORISATION CODE INVALID!!" Only two strings appear later in the list, which
are 0x25c, "AUTHORISATION CODE ACCEPTED...", and 0x25d, "ENTER A NAME FOR THE
SAVED FILE:". This suggests that the copy protection system was added very late
in development.

Changing the bytes `6016` back to `303c` will restore the file to its original
state. We can verify this by running the `checksum` program on disk 1, which
will verify the restored `playk240` executable as having the correct checksum of
$1cc3. You will need an unmodified version of Disk 1, however, or the checksum
will fail on the cracked version's packed intro file and other modified files.

The two bytes can be directly hex edited in either version of the executable
starting at location 0x4104 (decimal 16644). This can be used to disable the
authorisation code requirement on a legitimate copy, such as a harddisk install.
`6016` will disable the code requirement, and `303c` will enable it again.

### Directory comparison between v1.886 and v2.000

My version history for [Dungeons of
Avalon](https://tetracorp.github.io/dungeons-of-avalon/history/version-differences.html)
went more thoroughly into the file differences between various releases.
However, K240 versioning is relatively simple. It did not write save games to
its own disk, and in fact had a feature to prevent this, so most K240 disk
images are unmodified. There are fundamentally only two versions: v1.886, and
v2.000.

Here I'm comparing the v1.886 authorized download from [Gremlin Graphics
World](http://gremlinworld.emuunlim.com/amiga.htm) to the v2.00 SPS .ipf
release. The authorized release is cracked by TRSI & Zenith (TRZ); I assume the
latter to be unmodified from retail.

The file date on the Gremlinworld ADFs is 3 Sept 1997, suggesting someone ripped
these ADFs very early. CU Amiga magazine still existed when someone made ADFs of
their pirate copy of K240. The UAE emulator was only about two years old. The
Web Archive suggests that this zip had already been uploaded to the Gremlin
Graphics World by 14 August 2001.

It's clear that only file which changed between v1.886 and v2.000 is the main
game executable, `playk240` on disk 2. In other words, none of the supporting
game files actually changed. A convenient `checksum` program for this very
purposes exists on disk 3.  Now, the `checksum` program on disk 3 also changed
in v2.000, but only to update the checksum for the newer build of `playk240`.

There are some other differences, based on the file dates and md5sum. These are
limited to disk 1, and appear to all be caused by the pirate copy inserting its
cracktro message.

The cracktro program TRZ was added, and the startup-sequence modified to add it.
The `intro` executable shrunk from 20,740 bytes to 10,524, which appears to be
TRZ compressing it to make room for their 2,920 byte cracktro. Disassembly shows
that the smaller version is obfuscated while the larger isn't, suggesting that
it is indeed compressed. The v1.886 checksum program does not recognise these
changes, so we can infer that the compression is not part of the original disk.

The file dates on these give us a good sense of just how rapidly the game was
pirated. They're all dated 26 May 1994, while the build date embedded in the
executable is 20 May 1994, a Friday. This means the game was cracked and pirated
within six days of being finished, or four working days, including printing and
shipping the disks. The cracktro credits the supplier of the original disk to
"Troops & Troll".

One hypothesis is that v1.886 was an early build for magazine reviewers, as
there is a rumour that staff at one of the Amiga magazines leaked review copies
to pirate, leading some games to be pirated even before street date. However, on
further analysis I believe it to be the retail version, since magazines with
reviews would have already been published before the v1.886 build date
(see [development and release history](../history/development.html)).

Many files are dated 01-Feb-78, which looks like a default Amiga file date for
computers with no real-time clock. Notably, however, not all files are. Various
files are dated 20 Sept 1991, 2 Sept 1992, 2 Mar 1994, and 16 May 1994. It's
possible that many of the game's graphical assets were already in place in
September 1991; however, I suspect that these are default dates from an Amiga
with a hard disk but no real-time clock, which would therefore take its time
from the hard disk's OS install date.

### Directory comparison of the CU Amiga demo

All file dates on the CU Amiga coverdisk #77 demo of K240 are given the false
default date of 1978, so all we can say for certain is that it shipped with the
magazine dated March 1994, probably released in February 1994 as was the custom,
meaning that the disk was already completed in January or February 1994.

The 1978 dates actually span several months, so we might infer that whoever
wrote these files used an Amiga which was left switched on for several months at
a time. The latest is dated 20 July 1978.

Obviously, not all of the files from the full game are present on this one disk.

All six alien and planet graphics are there, unchanged, as are the six shop
blueprint files and several backgrounds: `wireplan.mgl`, `hologram.mgl`,
and `tetra.mgl`.

However, there are no voice files, outro graphics, or language files.
`welcome.mgl`, which I believe is the "welcome to sci-tek" audio, is not there,
and nor is `satpic.mgl`, since . None of the alien data files are there.

There are two unique demo files: `demo.mgl` and `demo2.mgl`. These are probably
the unique intro and outro screens. The file `scitek.mgl` is present, but it has
changed; it's 18,052 bytes instead of 18,035, for reasons I have yet to
discover.

### Executable analysis of the CU Amiga demo

The demo version of K240 distributed exclusively with CU Amiga magazine is
451,998 bytes, which is 17,780 or 17,776 bytes smaller than the final releases.
However, an in-depth analysis of the code needs to be done to determine the
differences between this demo and the final version.
