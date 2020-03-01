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

### File comparison between v1.886 and v2.000

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
it is indeed compressed. The v1.886 checksum program does not register these
changes, so we can infer that the compression is not part of the original disk.

The file dates on these give us a good sense of just how rapidly the game was
pirated. They're all dated 26 May 1994, while the build date embedded in the
executable is 20 May 1994, a Friday. This means the game was cracked and pirated
within six days of being finished, or four working days, including printing and
shipping the disks. The cracktro credits the supplier of the original disk to
"Troops & Troll".

I have a hypothesis that v1.886 was an early build for magazine reviewers, as
there is a rumour that staff at one of the Amiga magazines leaked review copies
to pirate, leading some games to be pirated even before street date. However, it
it also likely that was just a retail copy.

Many files are dated 01-Feb-78, which looks like a default Amiga file date for
computers with no real-time clock. Notably, however, not all files are. Various
files are dated 20 Sept 1991, 2 Sept 1992, 2 Mar 1994, and 16 May 1994. This
gives us a sense of how long the game took in development if some files,
specifically the background art, were already done in Sep 1991.

### Main game executable differences v.1886 to v2.000

More analysis needs to be done to determine what the differences are between the
two versions of the executable. The changes almost certainly consist of bugfixes
(see [bugs](../game-mechanics/bugs.html)).

Another change is that the pirate version has the copy protection check
disabled. The pirate version v1.886 main game executable fails the checksum on
its disk 3, which should be $1cc3. My hunch is that changing one or two
instructions (a few bytes) would recreate the original EXE, which can be
verified as it will pass the checksum.

### File comparison of the CU Amiga demo

All file dates on the CU Amiga coverdisk #77 demo of K240 are given the false
default date of 1978, so all we can say for certain is that it shipped with the
magazine dated March 1994, probably released in February 1994 as was the custom,
meaning that the disk was already completed in January or February 1994.

The 1978 dates actually span several months, so we might infer that whoever
wrote these files used an Amiga which was left switched on for several months at
a time. The latest is dated 20 July 1978.

Obviously, not all of the game files are present on this one disk.

All six alien and planet graphics are there, unchanged, as are the six shop
blueprint files and several backgrounds: `wireplan.mgl`, `hologram.mgl`,
and `tetra.mgl`

However, there are no voice files, outro graphics, or language files.
`welcome.mgl`, which I believe is the "welcome to sci-tek" audio, is not there,
and nor is `satpic.mgl`, since . None of the alien data files are there.

There are two unique demo files: `demo.mgl` and `demo2.mgl`. These are probably
graphics screens. The file `scitek.mgl` is present, but it has changed; it's
18,052 bytes instead of 18,035, for reasons I have yet to discover.
