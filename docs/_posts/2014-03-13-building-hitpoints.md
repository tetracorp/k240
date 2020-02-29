---
layout: post
title: "Building hitpoints"
categories: game-mechanics
---

Each building has a number of hit points. The table here lists each Terran
building's cost, hit points, build time and height (for the purpose of building
scaffold height and turret placement).

| Building                       |   Cost  | HP | BT | Ht|
|:-------------------------------|--------:|---:|---:|--:|
| Living Quarters                |   1,000 |  5 | 32 | 0 |
| Power Store                    |   1,500 | 34 | 32 | 0 |
| Storage Facility               |   1,500 | 24 | 20 | 0 |
| Anti-Missile Pod               |   7,000 | 16 | 36 | 0 |
| Solar Panel                    |     500 |  5 |  8 | 0 |
| Decontamination Filter         |   8,000 | 24 | 32 | 2 |
| Solar Generator                |   1,500 | 10 | 10 | 0 |
| Weapons Factory                |   4,400 | 24 | 32 | 0 |
| Mine                           |   4,000 | 20 | 32 | 0 |
| Satellite Silo                 |   5,000 | 10 | 24 | 0 |
| Screen Generator               |  20,000 | 36 | 52 | 0 |
| Ore Teleporter                 |  45,000 | 36 | 48 | 1 |
| Gravity Nullifier              |  35,000 | 24 | 52 | 1 |
| Deep Bore Mine                 |   5,500 | 20 | 36 | 0 |
| Missile Silo                   |   4,300 | 15 | 32 | 0 |
| Repair Facility                |  20,000 | 20 | 36 | 1 |
| Sensor Array                   |   3,500 | 15 | 36 | 3 |
| Plasma Turret                  |   5,500 | 20 | 30 | 0 |
| Photon Turret                  |   7,500 | 20 | 52 | 0 |
| Life Support                   |  13,000 | 24 | 48 | 2 |
| C.P.U                          |   8,000 | 36 | 40 | 3 |
| Seismic Penetrator             |  26,500 | 24 | 42 | 2 |
| Asteroid Engines               |  45,000 | 28 | 64 | 1 |
| Powerplant                     |  10,000 | 34 | 40 | 2 |
| Command Centre                 |   8,000 | 36 | 32 | 2 |
| Construction Yard              |   7,500 | 20 | 32 | 2 |
| Landing Pad                    |     300 |  5 | 16 | 0 |
| Laser Turret                   |   3,400 | 16 | 24 | 0 |
| Solar Matrix                   |   5,000 | 10 | 32 | 3 |
| Resiblock                      |   3,000 | 10 | 48 | 3 |
| Storage Tower                  |   3,000 | 32 | 40 | 2 |
| Protected Solar Matrix         |   7,200 | 20 | 48 | 3 |
| Protected Resiblock            |   8,500 | 20 | 56 | 3 |
| Protected Storage Tower        |   7,500 | 32 | 48 | 2 |
| Medical Center                 |   5,000 | 15 | 30 | 3 |
| Environment Control            |   3,200 | 34 | 20 | 2 |
| Protected Env/Ctrl             |   8,500 | 52 | 32 | 3 |
| Hydroponics                    |   7,000 | 24 | 16 | 3 |
| Hydration Plant                |   5,000 | 20 | 20 | 3 |
| Security Centre                |   4,500 | 15 | 24 | 2 |

### Taking and repairing damage

Buildings take damage when struck with weapons. Unless a Repair Facility exists
on the asteroid, a damaged building will __never__ repair itself. A colony which
survives one attack may fall in the next.

### Repair Facility

Each repair facility heals one point of damage every eight days (see [building
behaviour](building-behavior.html).)

### Building Armour
The Building Armour blueprint increases each building's maximum hit points
by 10. This does not automatically affect buildings constructed before acquiring
the blueprint, but a Repair Facility will retrofit old buildings to the new
maximum.

### Protected Buildings
In addition to the laser turret, most "protected" versions of buildings have
more hit points than their non-protected equivalent. The only one which does
not is the Protected Storage Tower.

The strongest Terran building in the game is the Protected Environment
Control, which has 52 hit points or 62 with Building Armour.
