---
layout: post
title: "Development and release history"
categories: history
---

This article chronicles the development and release of _K240_, a 1994 strategy
game published by Gremlin Graphics for the Commodore Amiga.

1. Table of Contents
{:toc}

### Development

#### Origins

K240 was fundamentally a sequel to _Utopia_, a land-based futuristic real-time
strategy game released around September 1991. The RTS genre was very new at this
point, and definitive titles like _Dune II_ and _Command & Conquer_ did not
exist yet; magazines interpreted _Utopia_ as a god game like _Populous_, while
Utopia's programmer Graeme Ing instead thought of it as a management strategy
simulation like _Sim City_.

[An interview](http://amr.abime.net/review_36809) with Graeme Ing appeared in
Amiga Action #28, the Jan 1992 issue; though remember that magazines often hit
the newsstands the month before their list date, and of course the articles were
written earlier than that. Graeme describes Utopia's influences as Larry Niven's
_Ringworld_ and Joe Haldeman's _The Forever War_.

He also announces two follow-ups to _Utopia_: an expansion disk, and a
fully-fledged sequel _Utopia 2_. Utopia 2 was planned to include more advanced
alien AI, would allow you to physically see the alien city, and would let you
target individual key buildings. Gremlin Graphics even offered five signed
copies of the game in a contest for innovative ideas.

At the end of 1991, Utopia 2 was still in the planning stage, but its release
was scheduled for the end of 1992.

#### 1992-1993

However, according to [a preview](http://amr.abime.net/review_20463) in
The One Amiga #59 (Aug 1993), development on Utopia 2 did not actually
start until May of 1992. This may be due to Graeme first spending four months
working on the Utopia expansion disk _Utopia: The New Worlds_, according to a
[review](http://amr.abime.net/review_3994) in the April 1992 issue of CU
Amiga.

The One #59 announces the game's name as K240 (though it conflates it with the
title of the Utopia 1 expansion, calling it _K240: The New Worlds_), with a
planned release date of December 1993. It is now revealed to be an asteroid
mining game, originally set in the
[Large Magellanic Cloud](https://en.wikipedia.org/wiki/Large_Magellanic_Cloud),
with a more military strategy gameplay.  Graeme Ing laments the features which
had to be cut for technical limitations, including more advanced AI and
null-modem type multiplayer. Another feature which didn't make it to the final
game was more special scenario goals, such as to find something before the
enemy does.

Screenshots in The One #93 show most of the game's recognizable visual features
already in place by August 1993. Noteworthy changes include more colourful
Terran ships, a different Protected Resiblock design, and a radically different
Transporter design with a matching blueprint in the ship build screen. The
Transporter builds in only 50 days, and Plasma Cannons cost only 1000.
The Fleet Battleship is slightly different, but has the usual color scheme.
We also see a green pagoda-like Terran building that doesn't appear in the final
game.

The next [preview](http://amr.abime.net/review_25444) is in Amiga Action #48 (Sep
1993), where Graeme describes the familiar count of 40 buildings, 7 ship types,
and 16 weapons. He describes three scenario missions which didn't make it into
the final game (disabling convoys, destroying shields, locating bases), and some
cut lore about the Empire being encroached upon by two alien races, causing a
resource shortage. We see the familiar missile control window. There is a fleet
window where readout showing a Combat Eagle with 150 armor points and an Assault
Fighter with 91; impossible configurations in the final release.

A [preview](http://amr.abime.net/review_19688) in Amiga Power #30 (Oct 1993)
suggests that you would have to invest time and money into research, though in
the final game you just buy them as blueprints. It's unclear if research was one
of the many features cut from the original design documents, or if this is just
a miscommunication.

#### 1994

In 1994, we begin to get into what can be determined from file dates in the
run-up to the game's release, as well as some more in-depth previews.

A short [preview](http://amr.abime.net/review_35944) in Amiga Format #56 (Feb
1994) has a screenshot which shows a few things of note. The layout of the
extracted buttons is identical to that of the PANEL cheat. The Construction Yard
sprite is similar to the CU Amiga demo rather than the final version. There are
two non-Terran large ships at a Terran colony. We can also see two numbers in
the top-left of the screen, some kind of debug information.

Meanwhile, file dates in the retail release show the finishing touches being put
on the game for distribution. In February and March 1994, disks 1 and 2 gain
startup-sequence files, and disk 3 gains a hard disk installer (adapted from the
installer for _HeroQuest 2: Legacy of Sorasil_).

A lot of unique development information is revealed in an in-depth
[preview](http://amr.abime.net/review_29004) in the March 1994 issue of CU
Amiga. Tony Dillon drove to Sheffield to interview Graeme Ing in person,
something CU Amiga often did, alllowing them access to some unique information,
in this case sprite sheets and some early game graphics.

The final version of the Transporter is shown, along with other original sprite
sheets. A screenshot of a very early test windowing system is also depicted. We
can see what looks like an alien Research Dome, but on a Terran colony; and an
earlier starfield graphic. Despite this archaic screenshot, we can recognize
Protected Solar Matrix, which one might otherwise have assumed to be a later
addition.

Something interesting appears in the screenshot of the alien load screen. We see
the Swixaran sprite, but what looks like the Ax'Zilanth homeworld (and some
placeholder text). This makes sense because both of these have the ID number #1,
being stored in `alienp1.mgl` and `planet1.mgl` respectively, despite neither
actually being used for alien #1 in the game.

The interview itself notes how the game was designed and developed, in an
on-and-off fashion for nearly two years at that point (consistent with the dates
of May 1992 to Feb 1994). The asteroid concept was added a few days after the
original design brief, which was to make a military strategic space game. The
full design specification was "immense", but was often changed during
development when testing revealed issues. An entirely new feature was added just
before the interview, though it's not certain what it was.

Included with that magazine is the K240 demo. More analysis of the executable
needs to be done to determine what features already existed in that version,
which was probably compiled in Jan/Feb 1994. The demo's win screen promises a
release in March 1994.

### Publication

On 29 April 1994, Commodore International declared bankruptcy. This did not
prevent the release of K240, but likely discouraged Gremlin Graphics from
releasing further games for the platform.

The final retail build of K240, version 1.886, was completed on Friday 20 May
1994 at 13:31. K240 was, presumably, released shortly thereafter.

A copy of the game was quickly acquired by someone credited as "Troops & Troll"
and provided to pirate groups TRSI & Zenith (TRZ), who quickly stripped the
manual copy-protection from the game and released a pirate copy on 26 May 1994.
In other words, the game was cracked not within six days of going on sale, but
within six days of the finished build.

A second build of the game, v2.000, was completed on 7 June 1994 at 11:15. This
version was almost certainly produced to fix bugs, though a more thorough
analysis will be necessary to determine which bugs were fixed.

Patrick Phelan is credited with providing the game's music. However, K240 has no
music. This is a mystery.

### Reception

Several magazines produced [reviews](http://hol.abime.net/2543/review) of K240
for their May 1994 issue. Almost certainly, these magazines received a review
copy of an earlier build, since most magazines printed their May issue in late
April.

This review build is very close to the v1.886 release, and the review copies
even included the game's manual. However, a clue that this is not the final
release is in the [review](http://amr.abime.net/review_9362) in issue 68 of The
One Amiga, which shows the game's win screen using the Intel screen background.
A likely reason for this is that the Swixaran win screen file, `outro3.mgl`, is
too big for the buffer and can crash the Amiga. The review copy probably
replaced all win screens with the Intel screen as a temporary fix; the final
release actually just uses the normal win screen graphic `outro1.mgl` for a
Swixaran win.

In an odd quirk, the [review](http://amr.abime.net/review_13565) by the
Dutch-language Amiga Magazine #29 (Sept-Oct 1994) uses gameplay screenshots from
the CU Amiga demo, not the final game. The giveaway is the asteroid layout and
the old sprite for the Environment Control (the white building at the right).

Reviews of K240 in the Amiga press were positive. CU Amiga rated it 91%,
receiving the CU Screen Star award for games recieving 85-92%, though missing
out on the ultimate Super Star award. The One Amiga rated it 90%; Amiga Format
84%; and Amiga Power 83%.

These review scores would later appear in an
[advertisement](https://www.lemonamiga.com/games/advert.php?id=625) for the game
published in various Amiga magazines. Of note are the outdated screenshots from
an earlier pre-release build of the game, which appear to pre-date the CU Amiga
demo. They include an older version of the Sci-Tek screen with a bright blue
background instead of the sophisticated graphics, and the byte font used in
_Utopia_. There are also screens depicting the use of the PANEL and ICBM cheat
codes. It also depicts the final box art; an earlier advertisement for Gremlin
depicted a variant with art of an asteroid colony floating in space.

K240 was criticized by some reviewers for its complexity and unorthodox user
interface. [It appears](https://www.youtube.com/watch?v=aD6d0cH0nNA&t=14m23s)
that some copies of the game included a flyer advertising a 30-minute tutorial
video for K240, recorded by Graeme Ing.

Unlike _Utopia_, K240 did not receive an expansion disk, and the finished
release did not include an option to load an optional scenario disk.

K240 received a remake/sequel, _Fragile Allegiance_, released for MS-DOS and
Windows 95 in December 1996. This game was written by a completely different
team of designers and programmers, but keeps most of K240's basic mechanics and
even maintains continuity with its lore. For example,
[the intro](https://www.youtube.com/watch?v=7ZCJ_16r8Sc)
cites Tetracorp's founding in the year 2221, consistent with
[the K240 manual](https://www.lemonamiga.com/games/docs.php?id=904),
which cites this as the year Tetracorp was founded to manufacture scoutships and
sensors for the Imperial Fleet. Assuming development on the PC version started
in mid-1994, it would have taken two and a half years.

### Detailed timeline
#### 1991

- __20 Sep 1991__: File dates for the game's voice clips and screen background
  art. All have file dates around 9am and within 8 minutes of each other,
  suggesting they were copied to floppy disk from an existing source.
  Based on interviews, this date seems unlikely to be accurate, and may be a
  false date from an Amiga with a hard disk installed in 1991, but no real-time
  clock, such as an A500.

#### 1992

- __Jan 1992__: Amiga Action #28 publishes an in-depth early preview of K240.
- __2 Sep 1992__: File dates for three rendered outro graphics displayed at the
  end of a scenario. Also the date of the disk icon. It's possible that this is
  the default date of an Amiga with a hard disk.

#### 1993

- __Aug 1993__: The One Amiga #59 publishes an in-depth preview of K240.
- __Sep 1993__: Amiga Action #48 publishes an in-depth preview of K240.
- __Sep 1993__: Amiga Action #48 publishes an in-depth preview of K240.
- __Oct 1993__: Amiga Power #30 publishes an in-depth preview of K240.
  Amiga Joker also publishes a preview.

#### 1994

- __Jan 1994__: Amiga Dream #3 publishes a preview of K240.
- __Feb 1994__: Amiga Format #56, Amiga Concept #1, and Amiga Joker publish
  previews of K240.
- __18 Feb 1994__: K240 icon file written.
- __28 Feb 1994__: Disk 1 startup-sequence written.
- __Mar 1994__: CU Amiga's March 1994 issue, though probably published in
  February. It includes Coverdisk #77, an exclusive playable demo of K240. The
  win screen gives its release date as March 1994, though the game would be
  delayed.  CU Amiga also gives a preview article.
- __2 Mar 1994__: Installer added to disk 3. Scenario folder created/modified,
  probably to put scenario files in. Game seems to be nearing completion.
- __4 Mar 1994__: Disk 2 startup-sequence written.
- __Apr 1994__: Amiga Computing #74 publishes an in-depth preview.
- __29 Apr 1994__: Final game launch icon added. Coincidentally, Commodore
  International declares bankruptcy.
- __May 1994__: Several Amiga magazines
  [review K240](http://hol.abime.net/2543/review). This appears to be an early
  review copy, newer than the CU demo based on the final design for Construction
  Yard, but it uses the Intel background for the Swixaran win screen.
- __16 May 1994__: A Monday. Directory `s` for startup-sequence written.
  Checksum program v1.0 written, according to internal version number.
  However, this program may have been written on 20th May, assuming it contains
  a correct checksum for the main game EXE.
- __20 May 1994__: A Friday. Final release build of K240 v1.886 main game
  executable, according to version string.
- __26 May 1994__: Pirate release completed by TRSI and Zenith.
- __7 Jun 1994__: K240 build v2.000 completed at 11:15, according to internal
  version number. Updated checksum program v.2.000 completed, and written to
  disk 3 at 16:33.

#### 1995 onward

- __Dec 1996__: PC sequel Fragile Allegiance released.
- __14 Oct 2001__: Someone makes a modified copy of the TRZ cracked release of
  disk 1 is made. It removes the TRZ cracktro.
