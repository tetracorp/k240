---
layout: post
title: "K240 CU Amiga demo"
categories: prototypes
---

![K240: The Demo](../images/demo.png "K240: The Demo")
{:right}

The March 1994 issue of CU Amiga Magazine came with coverdisk 77, an exclusive
demo version of K240. It provides an insight into the state of development of
the game as it neared completion, and has some interesting quirks.

This page is work-in-progress. A full analysis of the K240 demo executable has
yet to be made.

1. Table of Contents
{:toc}

## History

Amiga magazines were generally written around two months in advance of the cover
date. For example, old mailing list records note that the May 2000 issue of
Amiga Format, its final issue, already hit the newsstands by 6 April, while the
magazine was completed on 21 March.

The CU Amiga exclusive K240 demo, distributed with the March 1994 issue, must
therefore have been January 1994, around five months before the first completed
retail build.

The CU Amiga demo isn't quiet as exclusive as it may seem. The same demo was
given away with _Amiga Down Under_ #9 (May 1994), and was functionally identical
(including the CU Amiga branding on the title screen) except for some changed
file dates. Up to 300 copies of a demo were offered by French magazine _Amiga
Dream_ (May 1994), although it's unknown if this was the same demo or a later
French version.

## Building sprites

A number of game sprites reflect earlier versions than the finished release.

| Demo | Full game |
|------|-----------|
| ![construction_yard](../images/buildings/construction_yard_demo.png "construction_yard_demo") | [construction_yard](../images/buildings/construction_yard.png "construction_yard") |

| Demo | Full game |
|------|-----------|
| ![environment_control](../images/buildings/environment_control_demo.png "environment_control_demo") | [environment_control](../images/buildings/environment_control.png "environment_control") |

| Demo | Full game |
|------|-----------|
| ![protected_env_control](../images/buildings/protected_env_control_demo.png "protected_env_control_demo") | [protected_env_control](../images/buildings/protected_env_control.png "protected_env_control") |

| Demo | Full game | Blueprint |
|------|-----------|-----------|
| ![seismic_penetrator](../images/buildings/seismic_penetrator_demo.gif "seismic_penetrator_demo") |![seismic_penetrator](../images/buildings/seismic_penetrator.gif "seismic_penetrator") | |![Seismic penetrator blueprint](../images/seismic-penetrator-blueprint.gif "Seismic penetrator blueprint") |

The Seismic Penetrator cannot be acquired in the demo, but the building is still
in the game. The sprite is very different, and more closely resembles the
Seismic Penetrator's blueprint wireframe.

## Missing features

Several major gameplay options are missing from the demo. Some of these are
intentional limitations, but many probably reflect the unfinished state of the
game at this point. (Aspiring game developers should remember Hofstadter's Law:
It always takes longer than you expect, even when you take into account
Hofstadter's Law.)

Missing features include demolishing buildings, intercepting fleets, building
missiles, building ships, building an Orbital Space Dock, building or launching
satellites, Intelligence reports, establishing new colonies, loading or onto a
Transporter, selling ore to the Imperial Transporter, buying blueprints, gaining
money based on colonist count, loading and saving the game.

Only one alien is available. The voice sounds and intro are not available,
although this should be obvious given that the demo fits on a single disk
instead of three.

Cheat codes have been disabled, although game strings 

## Gameplay differences

You receive a notification when an enemy ship enters sensor range. The full game
has a voice clip for this (`enemyves.mgl` or "enemy vessel detected"), but it's
unused. This is probably because you can't intercept individual ships, and
they're always Scout Ships or Transporters that never attack your asteroid
intentionally.

You start with an established colony on a large asteroid. You have the Missile
Guidance System blueprint, and while you cannot build missiles, you have 20 each
Explosive, Area Explosive, Napalm, Hellfire, Scatter, and Vortex, and 10 Virus
missiles. You start with a large amount of money, some of which has already been
distributed into Construction and Intelligence, although Construction is the
only thing.

You can see the enemy asteroid surface without a spy satellite.

## Bugs

You can select an alien asteroid and fire their missiles. Another missile bug
lets you re-open the missile window while they're firing and increase the number
of missiles above 20.

Darkened window backgrounds disappear before the window does.
