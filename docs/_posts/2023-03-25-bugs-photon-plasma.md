---
layout: post
title: "Bugs: Photon vs Plasma"
categories: game-mechanics
---

![Photon cannon](../images/hardpoints/photon_cannon.png "Photon cannon"")
![Plasma cannon](../images/hardpoints/plasma_cannon.png "Plasma cannon"")
{:.right}

A [bug](bugs.html) in K240 is that the game regularly confuses whether Photon or
Plasma is the strongest ship-targeting weapon technology. Coupled with a lack of
transparency regarding weapon damage, this makes it hard to determine the
optimum strategy.

This article explores and explains the issue in detail.

In truth, this is as much for my own help. Every time I come back to this
project, I get confused as to how exactly the mix-up applies, and waste time
trying to re-prove it from first principles.

### What was already known

In the Shipyard build screen, the three ship-targeting weapons from left to
right are as follows:

| Image                                                                     | Weapon | Cost |
|---------------------------------------------------------------------------|--------|------|
| ![Laser](../images/hardpoints/laser.png "Laser"")                         | Laser  | 1000 |
| ![Photon cannon](../images/hardpoints/photon_cannon.png "Photon cannon"") | Photon | 4500 |
| ![Plasma cannon](../images/hardpoints/plasma_cannon.png "Plasma cannon"") | Plasma | 9000 |

The game's manual describes the Plasma Cannon as "The most powerful ship to ship
weapon".

Conversely, in ground turrets, it is consistently stated that Photon is the most
powerful. Sci-Tek calls Photon Turret "The best energy weapon available at this
time", as does the build screen. The manual concurs, both in blueprint
description and the building.

| Image                                                                     | Weapon        | BP Cost | Cost  | Power |
|---------------------------------------------------------------------------|---------------|---------|-------|-------|
| ![Laser turret](../images/hardpoints/laser_turret.png "Laser turret"")    | Laser Turret  | &mdash; | 3,400 |  2 MW |
| ![Photon turret](../images/hardpoints/photon_turret.png "Photon turret"") | Photon Turret | 100,000 | 7,500 |  5 MW |
| ![Plasma turret](../images/hardpoints/plasma_turret.png "Plasma turret"") | Plasma Turret |  60,000 | 5,500 |  3 MW |

Which is the most powerful?

### What the code says

Terran ship hardpoints number 05, 06 and 07 are all cannons. Manually editing
the starting stats of my starting Transporter in memory to give it four of
hardpoint 07, it shows in-game as Plasma Cannon. The internal numbers are
therefore clearly 05 Laser, 06 Photon Cannon, and 07 Plasma Cannon.

The code for the damage dealt by 

| ID | Weapon        | Damage |
|----|---------------|--------|
| 05 | Laser         |      2 |
| 06 | Photon Cannon |      8 |
| 07 | Plasma Cannon |      5 |

The effect is clear: Photon is the most powerful Terran ship to ship weapon,
despite being cheaper!

In alien ships, the hardpoints 05, 06, and 07 are also three types of cannon. We
never see alien hardpoint names, although by analogy to Terran ship weapons we
can nickname them 05 Laser, 06 Photon, and 07 Plasma. Here are their damage
values:

| ID | Alien       | Cannon 05 | Cannon 07 | Cannon 06|
|----|-------------|--:|--:|---:| 
| 01 | Kll-Kp-Qua  | 2 | 4 |  6 |
| 02 | Ore Eaters  | 2 | 4 |  6 |
| 03 | Ax'Zilanths | 3 | 5 |  8 |
| 04 | Tylarans    | 4 | 6 | 10 |
| 05 | Rigellians  | 5 | 7 |  0 |
| 06 | Swixarans   | 0 | 7 | 11 |

Note that the position of cannons 07 and 06 are swapped. This is the order their
damage values appear in the code, which is peculiar. Just like with Terran
weapons, cannon 06 is more powerful than cannon 07.

Supporting this designation, the Rigellians are the only species who do not have
a building in the slot of Photon Turret. They also have no ships with cannon 06,
and their cannon 06 is set to 0 damage.

In Terran building turrets, the code which determines turret damage values is as
follows:

| ID | Image                                                                     | Turret        | Damage |
|----|---------------------------------------------------------------------------|---------------|-------:|
| 18 | ![Plasma turret](../images/hardpoints/plasma_turret.png "Plasma turret"") | Plasma Turret |   5    |
| 19 | ![Photon turret](../images/hardpoints/photon_turret.png "Photon turret"") | Photon Turret |   8    |
| 28 | ![Laser turret](../images/hardpoints/laser_turret.png "Laser turret"")    | Laser Turret  |   2    |
|    |                                                                           | Any protected |   2    |

The damage values are the same as their ship to ship equivalents. The four
protected buildings act exactly as Laser Turret when it comes to firing.

The alien building list and Terran building list both line up, with the ID
numbers offset by 80 bytes and the turrets in the same positions in the list.
All alien turrets are just called Turrets, but it's clear that 

| ID  | Turret                   | Damage       |
|----:|--------------------------|--------------|
|  98 | Plasma Turret equivalent | As cannon 07 |
|  99 | Photon Turret equivalent | As cannon 06 |
| 108 | Laser Turret equivalent  | As cannon 05 |

In summary, it's clear: in all cases, **Photon deals more damage than Plasma**,
whether Terran or alien, ship to ship or turret.

### Testing to confirm

Thanks to a correct disassembly of the game, it's possible to write new debug
functions to aid in analysis. In particular, I created a function to show
on-screen whenever damage is dealt to a ship or building.

I start a game with the [Rigellians](../alien/rigellians.html). They only have
two types of which which deal damage: Laser, dealing 5, and Plasma, dealing 7. I
have a Scoutship which happens to have a Photon Cannon, dealing 8.

I send the Scoutship at the enemy colony. Someone fires, and it's 8 damage. My
ship has taken no damage, so this was my shot. The enemy then builds a new ship
and hits me for 5, destroying it. I bring in a replacement, and it is hit for 7.
An enemy scout returns, and my ship's Photon hits it for 8. I spawn in a new
ship with a Plasma Cannon, and see its cannon fire after a hit for 5.

For some reason, all my shots are one-hitting every enemy ship, which appears to
be a bug introduced by my code. Other than that, the damage values are all
in keeping with the code analysis.
