---
layout: post
title: "Differences between versions"
categories: history
---

K240 was released in two main versions: v1.886, the original retail release with
a build date of 20 May 1994; and v2.000, which appears to be a
[bug](../game-mechanics/bugs.html) fix, build date 7 June 1994. You can press
"V" during play to find out which version you have.

Additional non-retail versions of K240 are:

- A demo version distributed with CU Amiga issue #77 (Mar 1994) as an exclusive
  coverdisk. It appears to be based on an earlier build of the game circa
  January 1994 and has some differences: some notable bugs, and different graphics.
  I intend to disassemble this for comparison eventually.
- A demo version available by limited mail order offer in Amiga Dream #7, which
  may or may not be identical to the CU Amiga demo.
- At least one elusive version distributed to Amiga magazines as a review copy,
  mostly finished, and probably with a build date March 1994.
- Various cracked pirate releases of v1.886 and v2.000. Aside from removed
  copy-protection, cracktro, and trainers, these seem to be largely unchanged.

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

K240 has a manual protection code system which requires the entry of one of a
hundred words from the game's manual. The authorized free download of K240 is
based on a cracked pirate version of the v1.886 release, which made a single
two-byte change allowing any manual protection code to be accepted.

The change occurs at location 0x40ee (decimal 16622 bytes) in the `playk240`
executable, or at 0x40c6 in the disassembly. It is the same location for both
v1.886 and v2.000.

The original instruction is `MOVE.W #$025b,D0` (hexadecimal `303c 025b`) , which
places the ID number of the text string "AUTHORISATION CODE INVALID!!" into data
register D0. The cracked version has overwritten the first two bytes, `303c`,
with `6016`, which branches forward 24 bytes to the instructions normally
executed on entry of a correct code. All incorrect codes are therefore
effectively treated as correct codes.

The authorisation code requirement can be enabled or disabled by hex editing the
two bytes at location 0x40ee in the `playk240` executable. Setting the value to
`6016` disables it, which may be useful if you have a retail version but have
lost your manual. This is especially useful if you own a v2.000 copy of K240,
since the official download is v.1886 and suffers from the fleet bug.

Changing the two bytes back from `6016` to `303c` will restore the executable to
its original state. You can verify this by running the `checksum` program on
K240 disk 3, which will give a value of `$1cc3` for an unmodified v1.886
`playk240` file or `$2471` on v2.000, although the program may fail on a cracked
version due to other modified files, such as a packed `intro` file on disk 1.
I'm not sure why you would actually need to re-enable the manual code system,
but perhaps you need an unmodified original executable for
[speedrunning](../fun/speedrunning-k240.html), or just want to see what it looks
like when you input an incorrect code.

It is interesting to note that string 0x25b, "AUTHORISATION CODE INVALID!!", is
one of the last entries in the text string list. Only two strings appear later
in the list, which are 0x25c, "AUTHORISATION CODE ACCEPTED...", and 0x25d,
"ENTER A NAME FOR THE SAVED FILE:". This suggests that the copy protection
system was added very late in development.

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
IPF to be unmodified from retail.

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

One hypothesis was that v1.886 was an early build for magazine reviewers, as
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
meaning that the disk was already completed in January or February 1994, at
least three months before the v1.886 retail build.

The 1978 dates actually span several months, so we might infer that whoever
wrote these files used an Amiga which was left switched on for several months at
a time. The latest is dated 20 July 1978.

Obviously, not all of the files from the full game are present on this one disk.

All six alien and planet graphics are there, unchanged, as are the six shop
blueprint files and several backgrounds: `wireplan.mgl`, `hologram.mgl`,
and `tetra.mgl`.

However, there are no voice files, outro graphics, or language files.
`welcome.mgl`, which I believe is the "welcome to sci-tek" audio, is not there,
and nor is `satpic.mgl`, which isn't needed since the demo's spy satellite
feature is disabled. None of the alien data files are there (you can only fight
one alien in the demo, although the English language strings for the alien
descriptions are still in the game code).

There are two unique demo files: `demo.mgl` and `demo2.mgl`. These are probably
the unique intro and outro screens. The file `scitek.mgl` is present, but it has
changed; it's 18,052 bytes instead of 18,035, for reasons I have yet to
discover.

### Executable analysis of the CU Amiga demo

The demo version of K240 distributed exclusively with CU Amiga magazine is
451,998 bytes, which is 17,780 or 17,776 bytes smaller than the final releases.
However, an in-depth analysis of the code needs to be done to determine the
differences between this demo and the final version.

### Other demo versions
#### Amiga Down Under #9 Coverdisk demo

_Amiga Down Under_ issue #9 (May 1994) included a coverdisk with a demo of K240.
It is functionally identical to the CU Amiga demo, even including the special
graphics declaring the game a CU Amiga exclusive. The disk has a creation
date and time of 06-Apr-94 12:38:42, which is after CU Amiga released their
coverdisk on the March 1994 issue. The CU Amiga disk has a false creation date
of 1978 caused by being created on a standard Amiga without a real-time clock.
There are a few minor quirks about the exact disk structure, but effectively all
files and all file dates on the _Amiga Down Under_ coverdisk are exactly the
same as the CU Amiga dates.

#### Amiga Dream mail-order demo

[Amiga Dream issue 7](https://www.abandonware-magazines.org/affiche_mag.php?mag=13&num=1652&album=oui)
(May 1994) not only reviewed K240, devoted the following page to a mail-order
offer of 300 playable demos of K240 to give away. It's unknown what exactly this
demo contains. There's a chance it is just an identical copy of the CU Amiga
demo.

If you have a copy, it would be a great help if you can respond to
[this ticket](https://github.com/tetracorp/k240/issues/8) in the project's issue
tracker.

### Physical media differences

Some K240 disks have the label printed in orange, while others are printed in
white. Based on photos of copies of the game on eBay and elsewhere, the "white"
disks were accompanied with the K240 tutorial VHS flyer and a Gremlin prize draw
entry card, and their boxes had stickers attached advertising high review scores
(CU Amiga 91%, The One 90%). Both versions were widely available.

The most plausible explanation is that the white-label disks are from a second
print run. I have a hypothesis that all orange disks are v1.886, while white
disks are v2.000.

The Polish release of the game was published by a separate company, Licomp, and
had its own unique [box art](https://hol.abime.net/2543/boxscan) as a result,
which is largely a recreation of the English box art. Likewise with the manual.
Data-wise, the Polish disk contents are the same as the regular English release.

### Elusive Amiga magazine review copies

At least one build of the game was sent to Amiga magazines as a review copy in
March 1994, so that the magazines could review the game in time for their May
1994 issue. It's not the same build as the retail release, because that wasn't
completed until 20 May 1994, and magazines released their May issues in April.

Only a tiny number of review copies were distributed, and the fate of the disks
after the magaziness closed down is unknown&mdash;if you have a copy, please
[respond to the ticket](https://github.com/tetracorp/k240/issues/4) on the
project issue tracker, as you'd be a major help to the project.

What we do know about the review build is as follows:

- It is nearly complete to the retail v1.886 version. Screenshots show the final
  Construction Yard and Environment Control sprites, rather than the early
  sprites in the CU Amiga demo.
- The hard disk installer is included. This suggests a date of no earlier than 2
  March 1994, which is when the HD installer was added in the final release.
- It is English-only. [A review](https://www.abandonware-magazines.org/affiche_mag.php?mag=30&num=599&album=oui)
  in French magazine Joystick issue 49 (May 1994) shows only English-language
  screenshots (as do other French magazines' May 1994 reviews of K240), but
  promises that the final release will have a French translation.
- The victory screen background uses the intel screen background as a
  placeholder, as seen in The One issue 68.
- The intro disk appears to be included. Voice lines are in the game, according
  to the Joystick review. This suggests the review copy included all three
  disks.
- The finished manual appears to have been distributed with the review copy.
- Magazines which reviewed K240 for their May 1994 issue are assumed to have
  received a review copy. These included Amiga Action, Amiga Computing, Amiga
  Concept, Amiga Dream, Amiga Format, Amiga Power, CU Amiga, Joystick, and
  The One Amiga.
