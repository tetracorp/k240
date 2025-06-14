---
layout: post
title: "File formats"
categories: data
---

The following structure describes the file formats used by K240. It describes
what is in each of the game's files and how they are structured.

The process of documenting the game's file formats is incomplete and ongoing.

1. Table of contents
{:toc}

### k240\_1:data1.bin, data2.bin, data3.bin

Graphics and audio data read by the intro executable. They are compressed with
CrunchMania, although this has been obfuscated by replacing the first four bytes
(normally "CrM!" to denote a CrunchMania-packed file) with four spaces ("    ").
Extracted versions have been placed in the directory 
[intro_unpacked](https://github.com/tetracorp/k240/tree/main/data/intro_unpacked).

Filename  | Size    | Unpacked
----------|---------|----------
data1.bin | 217,326 | 266,744
data2.bin | 224,060 | 291,802
data3.bin | 377,074 | 417,270
TOTAL     | 818,460 | 975,816

### k240\_1:idfile

An ASCII text file consisting of the text "Hard disk ID file".

### k240\_1:intro

Intro sequence executable for K240. Only 20,720 bytes.

### k240\_1:s/startup-sequence

Typical Amiga startup-sequence which loads the intro, then runs the game from
disk 2. You can ignore disk 1 entirely and boot from disk 2.

```
k240_1:intro >nil: <nil:
k240_2:playk240 >nil: <nil:
```

### k240\_2:aliens/a1data1 - a6data1

Always 610 bytes. Sprite metadata table, consisting of 61 entries of 10 bytes
each. Each sprite entry has the following format:

| Size    | Data                    |
|---------|-------------------------|
| 4 bytes | Offset of start of data |
| 4 bytes | Offset of end of data   |
| 2 bytes | Sprite height           |

The 61 records are divided into four sections:

| Records | Data                    |
|--------:|-------------------------|
| 32      | Eight directional sprites each for each of the four small ships   |
| 16      | Eight sprites for both medium ships (Destructor/Terminator class) |
|  2      | Transporter and Fleet Battleship sprites                          |
| 11      | Missile silo launch animation.                                    |

Each of the six alien files relates to the equivalent alien in the list; e.g.
`a1data1` is the Kll-Kp-Qua, and `a6data1` is the Swixarans.

### k240\_2:aliens/a1data2 - a6data2

Contains the ship and building animation sprite data referenced in `a1data1`.
Stored as 16-color Amiga sprite format, with 4 bitplanes plus a fifth bitplane
as a sprite mask. The remainder of the file is the sprite for the alien Orbital
Space Dock.

Varies from 20,450 to 22,780 bytes.

### k240\_2:aliens/a1data3 - a6data3

Alien building sprite metadata and data. The first 400 bytes consist of 40
records of sprite data for 40 buildings. Buildings which do not apply to that
alien have a sprite height of 1 and a dummy sprite of 10 bytes (1x16).

The remainder of the file consists of the sprite graphics referenced in the
first part.

Varies from 4,240 to 8,450 bytes.

### k240\_2:aliens/a1data4.bin - a6data4.bin

Alien statistics. Always 1,928 bytes. The first 30 bytes appear to be stored as
part of the save game file.

| Type   | B | Description |
|--------|---|-------------|
| addr   | 4 | Pointer to memory location. Begins at $0000 0768. |
| word   | 2 | Alien ID number. |
| word   | 2 | Days between placing buildings. Tylaran=70, Swixaran=50, others=60. |
| word   | 2 | Build timer. Starts at 0 and increases +1 per day until it reaches the previous value, then resets to zero. |
| word   | 2 | Scout frequency? Varies by alien from 30 to 130 days. |
| word   | 2 | Colonization frequency. Varies 30-200 days. |
| word   | 2 | Missile build frequency. Varies 25-35 days (0 for Tylarans). |
| word   | 2 | Chance to ignore per-building softcap. Varies 10-25%. |
| word   | 2 | Missile attack delay counter. |
| word   | 2 | Missile attack delay counter. |
| word   | 2 | Alien laser cannon (#5) damage. Varies 2-5. |
| word   | 2 | Alien plasma cannon (#7) damage. Varies 4-7. |
| word   | 2 | Alien photon cannon (#6) damage. Varies 6-11. |
| word   | 2 | Sensor range for missiles. |
| word   | 2 | Sensor range for fleets. |
| word   | 2 | Turret cooldown. Varies 5-8 days. |
| byte   | 1 | Bitfield for alien-specific things (bit 2 = Swixaran asteroid cloaked) |
|Bldg[40]|400| 40 10-byte buildings as follows:<br>word (2) Name string<br>word (2) Description string (unused)<br>byte (1) Width<br>byte (1) Soft cap<br>byte (1) Build time (days)<br> byte (1) Height<br>byte (1) Intel type (0 General, 1 Defensive, 2 Offensive, 3 Power) |
| word[8]<!-- -->[4]| 64 | Build clusters. |
| word[11]| 22 | Chance to build each missile. |
| byte[11]| 11 | Yield of each missile as it appears on Intel report. (0 Low, 1 Med, 2 High, 3 other, ff unused) |
| word[2][8] | 32 | Build chance and build time for ships. |
| ShipB[8] | 192 | 8 24-byte ship stats as follows:<br>byte Armour<br>byte Speed<br>byte Hardpoints<br>byte Buildtime (ignored?)<br>4 bytes ore required (ignored for alien ships)<br>byte Ship ID<br>byte unknown<br>word Name (unused?)<br>word Cost (unused)<br>word Length (unused)<br>4 bytes unknown (unused?)<br>addr (4 bytes) extended data pointer. |
| unk | ? | Remainder currently unknown. Ship-related table, other alien data. |

See the individual alien descriptions from the index the main page for the
values which appear in each alien file.

### k240\_2:english.mgl, french.mgl, german.mgl

Text strings in each language, compressed in MGL format. Anyone creating an
unofficial translation for the game would need to modify one of these, then find
a way to re-pack it into MGL format. Alternatively, you could mod the game to
bypass the MGL loader and use uncompressed language files.

The first 1,210 bytes of each when uncompressed consists of 605 two-byte word
offsets for the beginning of each string in the file.

The rest of the file consists of 7-bit ASCII text strings, terminated by null
bytes. Newlines are usually represented by LF only on Amiga, but in this file
they are instead represented by `0xFF`. The file ends with `00 0a`. Non-English
letters are represented by the following values:

| Value |Char| 
|-------|----|
| 0x01  | Ç  |
| 0x02  | Ü  |
| 0x03  | Ä  |
| 0x04  | Ö  |
| 0x19  | █  |
| 0xFF  | \n |

See the [data directory](https://github.com/tetracorp/k240/tree/main/data/) for
the game strings.

### k240\_2:hologram.mgl, lang.mgl, tetra.mgl

IFF ILBM images, 320x200 pixels, compressed in MGL format.

| Filename       | Content                                            |
|----------------|----------------------------------------------------|
| `hologram.mgl` | Background of alien selection screen               |
| `lang.mgl`     | Language select screen at game start               |
| `tetra.mgl`    | Load/save screen background image featuring a ship |

See [extracted images (MGL files)](../data/images.html) for the images.

### k240\_2:idfile

An ASCII text file consisting of the text "Hard disk ID file".

It's not copied by the HD installer, so by checking for `idfile` the game can
tell if it's installed to hard disk or running from floppy disks. The main
reason you might want to do this is to determine whether the game must save to
floppy disk (in which case it saves to `DF0:` or to hard disk (in which case it
saves to `k240_2:`, which is assigned to the HD install location).

### k240\_2:playk240

Main game executable. The majority of this website is dedicated to analysis of
this one file. There are two known versions (see 
[differences between versions](../history/version-differences.html)):

| Version| Build date/time   | Bytes   |
|--------|-------------------|---------|
| v1.886 | 20 May 1994 13:25 | 469,764 |
| v2.000 | 7 June 1994 11:15 | 469,768 |

### k240\_2:s/startup-sequence

Typical Amiga startup-sequence. If you boot from disk 2 it will play the game
without the intro.

```
    k240_2:playk240 >nil: <nil:
```

### k240\_2:scenario/\*.mgl

Amiga sprite data, compressed in MGL format. The files `alienp1.mgl` -
`alienp2.mgl` contain the picture for that species. The files `planet1.mgl` -
`planet6.mgl` contain the rotating image of each alien's homeworld, stored as a
series of 64x53 frames.

The file numbers do not map directly to each alien as one might expect. Rather,
they apply as follows:

|Num| Alien       | Picture       | Planet        |
|---|-------------|---------------|---------------|
| 1 | Kll-Kp-Qua  | `alienp5.mgl` | `planet3.mgl` |
| 2 | Ore Eaters  | `alienp3.mgl` | `planet5.mgl` |
| 3 | Ax'Zilanths | `alienp2.mgl` | `planet1.mgl` |
| 4 | Tylaran     | `alienp6.mgl` | `planet6.mgl` |
| 5 | Rigellian   | `alienp4.mgl` | `planet4.mgl` |
| 6 | Swixarans   | `alienp1.mgl` | `planet2.mgl` |

See [extracted images (MGL files)](../data/images.html) for the images.

### k240\_3:Disk.info

Amiga icon file.

### k240\_3:Install-k240, Install-k240.info

K240 hard disk install script, written by Graeme Ing. Based on the _HeroQuest 2:
Legacy of Sorasil_ HD installer script by Kevin Dudley. It won't install unless
you have at least 2,100,000 bytes free. The .info file is its icon, which
launches it with the included Installer program.

### k240\_3:Installer

Amiga hard disk Installer program v1.24 (1.9.92).

### k240\_3:checksum

An Amiga executable which verifies files on the disks to a pre-calculated
checksum.

### k240\_3:k240

A script to launch the game from from hard disk. It assigns all K240 disk volume
labels to the current directory, plays the intro, then plays the game. You can
skip the intro either by commenting out the intro line, or (undocumented
feature) by holding the left mouse button while the game is loading. The actual
game executable is called `playk240`.

```
; K240 Hard Disk Startup Sequence
;

ASSIGN "k240_1:" ""
ASSIGN "k240_2:" ""
ASSIGN "k240_3:" ""

k240_1:intro <nil: >nil:
k240_2:playk240 <nil: >nil:
```

### k240\_3:k240.inf

Amiga icon for "k240". Will be renamed to `k240.info` when copied.

### k240\_3:\*.mgl

IFF ILBM images, 320x200 pixels, compressed in MGL format.

| Filename      | Content                                    |
|---------------|--------------------------------------------|
| `outro1.mgl`  | Victory screen                             |
| `outro2.mgl`  | Defeat screen                              |
| `outro3.mgl`  | Victory screen against Swixarans (unused)  |
| `satpic.mgl`  | Intel screen background                    |
| `scitek.mgl`  | Sci-Tek screen background                  |
| `wireplan.mgl`| Alien selection screen background          |

See [extracted images (MGL files)](../data/images.html) for the images.

### k240\_3:shop1.mgl - shop6.mgl

Amiga sprite data compressed in MGL format. Each file contains six wireframe
graphics for blueprints appearing on the Sci-Tek screen, except for `shop6.mgl`
which has only four, since there are only 34 blueprints in total.

See [extracted images (MGL files)](../data/images.html) for the images.

### k240\_3:speech/\*.mgl

Speech audio files. Compressed in MGL format.

| Filename       | Sound                            |
|----------------|----------------------------------|
| `ALERT.MGL`    | "Alert, alert"                   |
| `ASTDESC.MGL`  | "Asteroid discovered"            |
| `ATTENTIO.MGL` | "Attention"                      |
| `COLLISIO.MGL` | "Collision imminent"             |
| `CREPORT.MGL`  | "Colonization report"            |
| `ENEMYVES.MGL` | "Enemy vessel detected" (unused) |
| `EQUIPMAL.MGL` | "Equipment malfunction"          |
| `FARRIVE.MGL`  | "Fleet arrived"                  |
| `FDEPLOY.MGL`  | "Fleet deployment detected"      |
| `FREPORT.MGL`  | "Fleet report"                   |
| `GREPORT.MGL`  | "Geological report"              |
| `HOSFLT.MGL`   | "Hostile fleet approaching"      |
| `INBOUND.MGL`  | "Inbound missile"                |
| `MAGSTORM.MGL` | "Magnetic storm"                 |
| `METEOR.MGL`   | "Meteor storm"                   |
| `MLAUNCH.MGL`  | "Missile launch detected"        |
| `RADWARN.MGL`  | "Radiation warning"              |
| `RESOURCE.MGL` | "Resource deficiency"            |
| `SCREPORT.MGL` | "Scout report"                   |
| `SECREP.MGL`   | "Security report"                |
| `welcome.mgl`  | "Welcome to Sci-Tek"             |

### Save game format

Save games are stored in files `k240.1`, `k240.2`, `k240.3`, and `k240.4`. These
are stored in `DF0:` if playing from floppy disk or `k240_2:` (nominally disk 2,
but actually the game's directory on the hard disk) if playing from hard disk.

For a full description, see [save game format](save-game-format.html).

Eight chunks of the game's memory are saved:

| Offset  | Length | Description |
|--------:|-------:|-------------|
|       0 |     18 | Save game name (16 bytes) and current alien ID (2 bytes). |
|      18 |     30 | Alien variables (`a1data{1-6}.bin` +4 bytes, for 30 bytes). |
|      48 | 55,810 | Miscellaneous game state: Transporter cargo, extracted buttons, asteroid maps (53,856 bytes for 24 asteroids at 34x33 words each), current money, Imperial transporter timer, asteroid hotkeys, comet locations, blueprints owned, date, numerous others. |
|  55,858 | 37,800 | Ships. 700 ships at 54 bytes per ship. "Ships" includes missiles, satellites, and Vortex storms. |
|  93,658 | 33,600 | Buildings. 14 bytes per building, 100 buildings per asteroid, 24 asteroids. |
| 127,258 | 18,000 | Asteroids. 24 asteroids at 750 bytes each. |
| 145,258 |  1,920 | Building totals. 24 asteroids, 80 buildings per asteroid (40 Terran, 40 alien) |
| 147,178 |  2,336 | Terran fleets. |
| 149,514 |  2,336 | Alien fleets.  |
|         |151,850 | TOTAL |

