---
layout: post
title: "#3: Ax'Zilanths"
categories: alien
---

![planet1.mgl](../images/planet1.gif "planet1.mgl")
{:.right}

![alienp2.mgl](../images/alienp2.png "alienp2.mgl")

The Ax'Zilanths are the closest equivalent to the Terran player.

1. Table of Contents
{:toc}

### Unique traits

They require air and food, although they survive longer without air than the
Terran colonists (3 population loss per day, rather than 100% of the
population). They are not immune to radiation like some other aliens, and cannot
gain new colonists if there is 50% radiation or higher, although radiation will
never kill colonists.

If food, water and radiation requirements are met, the Ax'Zilanths gain one new
colonist each day.

The possess the unique ability to adapt to Virus missiles. The second Virus
missile fired by the player will have no effect. This is true even if you fire
at yourself or an unoccupied asteroid.

The AI for this alien sets a flag when it loses a colony due to its population
reducing to zero due to lack of Personnel Podules, Atmospheric Regulator or
Nutrient Podule (though not if the colony explodes due to Mega or asteroid
collision). The exact actions it takes in response to this have yet to be
analyzed.

Their technology allows them to teleport their asteroid. A discovered asteroid
becomes undiscovered after it teleports (see Mass Displacement Podule). They
also have a missile which can intercept and neutralize incoming missiles.

### Buildings

Each alien building has a name, a type (as it counts on a spy satellite report),
Hit Points, build time (in days), a height (for the purpose of scaffold), a
width (1, for one-square, or 4 for a 2x2 building), a softcap (buildings marked
! have a hard cap instead), and the building at the equivalent position in the
Terran building list.

| Name                      | Type    |  HP |  BT | H | W |  Cap | Equivalent
|:--------------------------|:--------|----:|----:|--:|--:|-----:|:-----------------------
| Personnel Podule          | General |  16 |  20 | 3 | 1 |    6 | Living Quarters
| Energy Accumulator        | Power   |  20 |  12 | 1 | 1 |    4 | Power Store
| Resource Podule           | General |  22 |  10 | 3 | 1 |    4 | Storage Facility
| Atomiser                  | General |  32 |  25 | 2 | 1 |    4 | Decontamination Filter
| Engineering Plant         | Offense |  32 |  30 | 3 | 1 |    2 | Weapons Factory
| Ore Extractor             | General |  20 |  12 | 1 | 1 |    6 | Mine
| Defence Shield            | Defence |  36 |  60 | 2 | 1 |    4 | Screen Generator
| Repulse Generator         | Defence |  32 |  44 | 2 | 1 |    1!| Gravity Nullifier
| Missile Silo              | Offense |  10 |  25 | 1 | 1 |    4 | Missile Silo
| Sensory Matrix            | General |  10 |  15 | 3 | 1 |    1!| Sensor Array
| Turret                    | Offense |  20 |  20 | 1 | 1 |    4 | Plasma Turret
| Turret                    | Offense |  24 |  40 | 1 | 1 |    4 | Photon Turret
| Atmospheric Regulator     | General |  20 |  20 | 2 | 1 |    3 | Life Support
| Propulsion Unit           | Defence |  32 |  55 | 2 | 4 |    1!| Asteroid Engines
| Reactor                   | Power   |  26 |  51 | 3 | 4 |    2 | Powerplant
| Strategy Control          | General |  36 |  50 | 3 | 4 |    1!| Command Centre
| Spacecraft Dock           | Offense |  24 |  25 | 2 | 4 |    2 | Construction Yard
| Stabilising Platform      | General |   8 |  15 | 0 | 1 |    4 | Landing Pad
| Science Podule            | General |  16 |  14 | 3 | 1 |    3 | ~~Medical Centre~~
| Nutrient Podule           | General |  16 |  15 | 3 | 1 |    6 | Hydroponics
| Mass Displacement Podule  | Defence |  32 | 100 | 1 | 1 |    1!| ~~Hydration Plant~~
| Subspace Detectors        | Defence |  24 |  25 | 3 | 1 |    1!| ~~Security Centre~~

Atmospheric Regulator
: Required for life. If there is not at least one Atmospheric Regulator, the
colony loses 3 population per day. However, since Nutrient Podule is checked
first, a colony with neither of those buildings only suffers the lesser penalty
of losing 1 per day.

Atomiser
: Reduces radiation by 30%. The colony must have no more than 40% radiation for
population growth, which is one per day.

Defence Shield
: A Screen Generator. Presumed to work the same as Terran Screen Generator,
which reduces damage to all covered buildings by half.

Energy Accumulator
: At least one Energy Accumulator or Reactor is needed to power Repulse
Generator, Propulsion Unit and Ore Extractor.

Engineering Plant
: Required to build ships and missiles.

Mass Displacement Podule
: Allows asteroid to teleport. It can teleport in response to incoming missiles,
if there are no Interceptor missiles left. It also has a 1% chance to teleport
on an occasion when it would normally fire missiles. More research is required.

Missile Silo
: Required to build or launch missiles.

Nutrient Podule
: Required for life. If there is not at least one Nutrient Podule, the colony
loses 1 population per day.

Ore Extractor
: Mines two units each of five randomly selected ores per day. Can mine any ore.
Building multiple Ore Extractors has no effect. Requires one Reactor or Energy
Accumulator to function. At least one Ore Extractor or Resource Podule is
necessary to build ships.

Personnel Podule
: Provides housing for up to 100 colonists. If there are no Personnel Podules,
the colony is destroyed.

Propulsion Unit
: Appears in the Asteroid Engines slot, suggesting this is an Asteroid Engines.
Requires at least one Reactor or Energy Accumulator to function.

Reactor
: At least one Energy Accumulator or Reactor is needed to power Repulse
Generator, Propulsion Unit and Ore Extractor. A Reactor is required to build
missiles.

Repulse Generator
: Appears in the Gravity Nullifier slot, suggesting that this is a Gravity
Nullifier. Requires at least one Reactor or Energy Accumulator to function.

Resource Podule
: Equivalent to Storage Facility. At least one Ore Extractor or Resource Podule
is necessary to build ships, but the game does not track mined ore.

Science Podule
: Unknown.

Sensory Matrix
: Increases the chances of spotting Terran spy satellites. The base chance is 1%
plus a cumulative 1% per day, and each additional Sensory Matrix and Subspace
Detectors adds another chance per day, although a colony will never build more
than one of each, for a maximum of three chances per day.

Spacecraft Dock
: Shipyard. Required to build ships, with a cap of 4 shipyards.

Stabilising Platform
: Landing Pad. At least one is required to build ships.

Strategy Control
: Equivalent to Command Centre. Required to start new colony.

Subspace Detectors
: Increases the chances of spotting Terran spy satellites. The base chance is 1%
plus a cumulative 1% per day, and each additional Sensory Matrix and Subspace
Detectors adds another chance per day, although a colony will never build more
than one of each, for a maximum of three chances per day.

Turret
: A plasma turret which deals 5 damage, the same as Terran plasma turrets.
Fires on a 6-day cooldown. The Ax'Zilanths do not use Laser turrets.

Turret
: A photon turret which deals 8 damage, the same as Terran plasma turrets.
Fires on a 6-day cooldown.

### Building strategy

Each Ax'Zilanth colony attempts a new build every 60 days. They do not require
any currency or resources to produce buildings. Unless there is an urgent need,
they will randomly build one of the following clusters of four buildings:

* 0: Reactor, Turret (Plasma), Turret (Photon), Missile Silo
* 1: Atmospheric Regulator, Personnel Podule, Reactor, Nutrient Podule
* 2: Sensory Matrix, Repulse Generator, Energy Accumulator, Mass Displacement Podule
* 3: Propulsion Unit, Spacecraft Dock, Stabilising Platform, Engineering Plant
* 4: Strategy Control, Energy Accumulator, Personnel Podule, Nutrient Podule
* 5: Personnel Podule, Atomiser, Subspace Detectors, Stabilising Platform
* 6: Ore Extractor, Ore Extractor, Resource Podule, Missile Silo
* 7: Defence Shield, Science Podule, Reactor, Missile Silo

Each building has a 100% chance to build until it reaches the cap, but there is
a 15% chance per building to ignore the cap and build anyway. The exceptions are
the Mass Displacement Podule, Propulsion Unit, Repulse Generator, Sensory
Matrix, Strategy Control, and Subspace Detectors, which have a hard cap of 1 per
asteroid.

If a colony lacks an Atmospheric Regulator or Nutrient Podule, or has neither
Reactors nor Energy Accumulators, they make it a priority to build the following
cluster:

* 1: Atmospheric Regulator, Personnel Podule, Reactor, Nutrient Podule

### Missiles

Each asteroid attempts to build missiles every 30 days. They must have a Reactor
(Energy Accumulators are not sufficient), Engineering Plant, and Missile Silo to
build missiles. They roll on the following percentile table and built that
missile, to a maximum of 5. The yield listed is as shown on an intel survey.

| Missile         | Build  | Yield |
|-----------------|-------:|------:|
| Area Explosive  |   23%  | Med   | 
| Scatter         |   18%  | Med   | 
| "Interceptor"   |   15%  | Other | 
| Vortex          |   8%   | Med   | 
| Hellfire        |   8%   | High  | 
| "Static Inducer"|   8%   | Other |
| Virus           |   7%   | Other | 
| Stasis          |   5%   | Other | 
| Nuclear         |   5%   | High  | 
| Mega            |   3%   | High  | 

"Interceptor"
: Replaces the Antivirus. Intercepts and neutralizes incoming warheads. When a
missile strike is incoming, 1-4 of these are launched in response. They have
been observed self-destructing before leaving the asteroid, which may be a
custom trigger to avoid actually firing one as an offensive missile against a
Terran colony, where it would have the effect of an Antivirus.

"Static Inducer"
: Replaces the Explosive. Causes a Static Inducer effect in all ships.
More testing required.

Trivia: 

* The Ax'Zilanths do not use Napalm, but do use Hellfire. They are the only
  alien to use Hellfire.
* They are the only alien to use the Vortex missile. Other aliens use those
  slots, but only as custom missiles.
* They do not use Explosive or Antivirus, since special code replaces these
  warheads.

### Ships

Each ship an armor value, speed, number of hardpoints (sometimes erroneous),
ID number in the game code, and up to six hardpoints. The names here are
arbitrary and do not appear in the code.

Name                  | Armor | S | H | ID | HP1| HP2| HP3| HP4| HP5| HP6|
----------------------|------:|--:|--:|:---|----|----|----|----|----|----|
"Fighter"             |    30 | 2 | 2 | 3c | 06 | 09 |    |    |    |    |
"Light Cruiser"       |    40 | 2 | 3 | 3d | 07 | 09 | 01 |    |    |    |
"Heavy Cruiser"       |    40 | 1 | 2 | 3e | 06 | 05 | 00 | 02 |    |    |
"Scoutship"           |    15 | 1 | 1 | 3f | 06 |    |    |    |    |    |
"Light Bomber"        |    50 | 1 | 4 | 40 | 09 | 07 | 03 | 01 |    |    |
"Heavy Bomber"        |    60 | 1 | 5 | 41 | 09 | 07 | 03 | 01 | 04 |    |
"Transporter"         |    35 | 0 | 2 | 42 | 06 | 06 |    |    |    |    |
"Battleship"          |    90 | 0 | 6 | 43 | 07 | 06 | 03 | 01 | 07 | 03 |

Ship $3c "Fighter"
: A fast 30 Armor ship with a Photon Cannon (8 damage) and Warp Generator.
Warp Generator phases ship out for three days and back in for two. Due to a bug,
however, being phased out has no effect.

Ship $3d "Light Cruiser"
: A fast 40 Armor ship with a a Plasma Cannon (5 damage), Warp Generator, and
Disruptor.

Ship $3e "Heavy Cruiser"
: A slower 40 Armor ship with a Photon Cannon (8 damage), Warp Generator, Ion
Cannon and Disruptor. Listed in the game code has having two hardpoints,
although it has four.

Ship $3f "Scoutship"
: A slower 15 Armor ship with a Photon Cannon (8 damage). The weakest ship. The
Ax'Zilanths and Rigellians are the only two species with a slow scout ship like
this. The only small Ax'Zilanth ship without a Warp Generator.

Ship $40 "Light Bomber"
: A slower 50 Armor ship with a Warp Generator, Plasma Cannon (5 damage), Chaos
Bomb and Disruptor.

Ship $41 "Heavy Bomber"
: A slower 60 Armor ship with a Warp Generator, Plasma Cannon (5 damage), Chaos
Bomb, Disruptor and Vortex Mine. Identical to the previous ship except for
higher Armor and a Vortex Mine.

Ship $42 "Transporter"
: A slow 35 Armor ship with two Photon Cannons (8 damage). A typical
Transporter.

Ship $43 "Battleship"
: A slow 90 Armor ship with six hardpoints: two Plasma Cannons (5 damage),
two Chaos Bombs, a Photon Cannon (8 damage) and a Disruptor.

### Starting resources

When facing the Ax'Zilanths, the player starts with the following resources:

* Cash: 250,000 credits (default)
* Blueprints: Gravity Nullifier, Shield X40, Solar Matrix

The alien colony begins with the following building clusters:

* 1: Atmospheric Regulator, Personnel Podule, Reactor, Nutrient Podule
* 4: Strategy Control, Energy Accumulator, Personnel Podule, Nutrient Podule
* 2: Sensory Matrix, Repulse Generator, Energy Accumulator, Mass Displacement Podule

They start with the following ships:

* $3d "Light Cruiser" x5
* $3f "Scoutship x1"
* $42 "Transporter" x2
* $43 "Battleship" x1

### Colonization strategy

Each Ax'Zilanth colony considers starting a new colony every 35 days.
The colonization countdown freezes if there is no Strategy Control.

A colony ship carries 100 population, altough this does not decrease the
population on the asteroid.

A new colony builds the following cluster of buildings:

* 1: Atmospheric Regulator, Personnel Podule, Reactor, Nutrient Podule

### Mining strategy

The Ax'Zilanth mine every day. If there is at least one Ore Extractor, and at
least one Reactor or Energy Accumulator, the colony mines five times, and
depletes two units of a random ore each time. They can mine all ten ores types.

Building additional Ore Extractors has no effect, although they will build as
many as six before hitting the soft cap. The amount of ore mined is not stored
anywhere.
