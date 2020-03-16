---
layout: post
title: "Miscellaneous features"
categories: game-mechanics
---

Here are a few minor undocumented features.

### Skip intro

Hold the left mouse button to skip the intro sequence.

This is mainly useful on the hard disk install. When playing from floppy disk,
you can skip the intro just by booting from disk 2.

### Pause Tetracorp slogans

In the new game / load game screen, a series of advertising slogans for
Tetracorp appear. If you hold a mouse button, the current slogan will stay on
screen until you let go.

Another overlooked feature is how the text ticker makes sounds. It only makes
the tick sound when playing consonants, not vowels. This gives the ticker
something resembling the cadence of human speech.

### Land on hangar

If you order a ship to Land on Surface, it randomly chooses a square to ladn on.
If it chooses a square with a hangar in it, it will land _in_ the hangar
instead.

### Free temporary gravity nullifier

At the start of the game, for a limited time period, your colony and the enemy
colony is affected by a temporary Gravity Nullifier effect. This is hard to
notice, because it has normally worn off by the time you buy the Asteroid
Tracker blueprint that lets you see asteroid speed.

### Asteros half-life

Asteros depletes at the rate of one unit every four days. This starts from the
moment you colonize the asteroid. It's not clear whether this is meant to
represent radioactive decay, or is just a bug in the Powerplant code. See
[building behaviour](../game-mechanics/building-behaviour.html) for the strange
way Powerplant functions.

### Ax'Zilanth viral resistance

When fighting against the Ax'Zilanth, the second Virus missile you fire against
an asteroid has no effect. That alien appears to adapt after the first missile.
This applies even if you fire a second virus at yourself.

### Where are my 5,000,000 credits?

If you defeat the final alien, you receive a unique message of congratulation
with an award of 5,000,000 credits. The game then freezes at that point.
Checking the game code, however, it doesn't actually give you 5,000,000 credits.

You don't have to play all the aliens in order to get the win screen, just beat
the last one. The game doesn't keep track of which aliens you beat anywhere.

### Keyboard controls

These are documented in the manual, but some players may not be aware of them.

* Press _spacebar_ to toggle between building view and flat view
* Press _S_ to enable the Ship cursor for clicking on ships.
  Press again to return to the standard cursor.
* Press _D_ to enable to Demolish cursor (green bomb) for
  demolishing buildings. Press again to return to the standard cursor.
* Press the left and right cursor keys to rotate the asteroid. Useful for making
  the icons visible after a PANEL cheat.
