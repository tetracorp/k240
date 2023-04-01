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
: ![Atmospheric Regulator](../images/alien_bldg/axz_atmospheric_regulator.gif "atmospheric regulator"){:.left} Required for life. If there is not at least one Atmospheric Regulator, the
colony loses 3 population per day. However, since Nutrient Podule is checked
first, a colony with neither of those buildings only suffers the lesser penalty
of losing 1 per day.

Atomiser
: ![Atomiser](../images/alien_bldg/axz_atomiser.gif "atomiser"){:.left} Reduces radiation by 30%. The colony must have no more than 40% radiation for
population growth, which is one per day.

Defence Shield
: ![Defence Shield](../images/alien_bldg/axz_defence_shield.gif "defence shield"){:.left} A Screen Generator. Presumed to work the same as Terran Screen Generator,
which reduces damage to all covered buildings by half.

Energy Accumulator
: ![Energy Accumulator](../images/alien_bldg/axz_energy_accumulator.gif "energy accumulator"){:.left} At least one Energy Accumulator or Reactor is needed to power Repulse
Generator, Propulsion Unit and Ore Extractor.

Engineering Plant
: ![Engineering Plant](../images/alien_bldg/axz_engineering_plant.gif "engineering plant"){:.left} Required to build ships and missiles.

Mass Displacement Podule
: ![Mass Displacement Podule](../images/alien_bldg/axz_mass_displacement_podule.gif "mass displacement podule"){:.left} Allows asteroid to teleport. It can teleport in response to incoming missiles,
if there are no Interceptor missiles left. It also has a 1% chance to teleport
on an occasion when it would normally fire missiles. If the asteroid gets too
close to the edge of the screen and does not currently benefit from a gravity
nullifier effect, it may also teleport to avoid zooming off the edge of the
screen.

Missile Silo
: ![Missile Silo](../images/alien_bldg/axz_missile_silo.gif "missile silo"){:.left} ![axz_missile_silo_anim](../images/alien_ships/axz_missile_silo_anim.gif "axz_missile_silo_anim"){:.left}
Required to build or launch missiles.

Nutrient Podule
: ![Nutrient Podule](../images/alien_bldg/axz_nutrient_podule.gif "nutrient podule"){:.left} Required for life. If there is not at least one Nutrient Podule, the colony
loses 1 population per day.

Ore Extractor
: ![Ore Extractor](../images/alien_bldg/axz_ore_extractor.gif "ore extractor"){:.left} Mines two units each of five randomly selected ores per day. Can mine any ore.
Building multiple Ore Extractors has no effect. Requires one Reactor or Energy
Accumulator to function. At least one Ore Extractor or Resource Podule is
necessary to build ships.

Personnel Podule
: ![Personnel Podule](../images/alien_bldg/axz_personnel_podule.gif "personnel podule"){:.left} Provides housing for up to 100 colonists. If there are no Personnel Podules,
the colony is destroyed.

Propulsion Unit
: ![Propulsion Unit](../images/alien_bldg/axz_propulsion_unit.gif "propulsion unit"){:.left} Appears in the Asteroid Engines slot, suggesting this is an Asteroid Engines.
Requires at least one Reactor or Energy Accumulator to function.

Reactor
: ![Reactor](../images/alien_bldg/axz_reactor.gif "reactor"){:.left} At least one Energy Accumulator or Reactor is needed to power Repulse
Generator, Propulsion Unit and Ore Extractor. A Reactor is required to build
missiles.

Repulse Generator
: ![Repulse Generator](../images/alien_bldg/axz_repulse_generator.gif "repulse generator"){:.left} Appears in the Gravity Nullifier slot, suggesting that this is a Gravity
Nullifier. Requires at least one Reactor or Energy Accumulator to function.

Resource Podule
: ![Resource Podule](../images/alien_bldg/axz_resource_podule.gif "resource podule"){:.left} Equivalent to Storage Facility. At least one Ore Extractor or Resource Podule
is necessary to build ships, but the game does not track mined ore.

Science Podule
: ![Science Podule](../images/alien_bldg/axz_science_podule.gif "science podule"){:.left} Unknown.

Sensory Matrix
: ![Sensory Matrix](../images/alien_bldg/axz_sensory_matrix.gif "sensory matrix"){:.left} Increases the chances of spotting Terran spy satellites. The base chance is 1%
plus a cumulative 1% per day, and each additional Sensory Matrix and Subspace
Detectors adds another chance per day, although a colony will never build more
than one of each, for a maximum of three chances per day.

Spacecraft Dock
: ![Spacecraft Dock](../images/alien_bldg/axz_spacecraft_dock.gif "spacecraft dock"){:.left} Shipyard. Required to build ships, with a cap of 4 shipyards.

Stabilising Platform
: ![Stabilising Platform](../images/alien_bldg/axz_stabilising_platform.gif "stabilising platform"){:.left} Landing Pad. At least one is required to build ships.

Strategy Control
: ![Strategy Control](../images/alien_bldg/axz_strategy_control.gif "strategy control"){:.left} Equivalent to Command Centre. Required to start new colony.

Subspace Detectors
: ![Subspace Detectors](../images/alien_bldg/axz_subspace_detectors.gif "subspace detectors"){:.left} Increases the chances of spotting Terran spy satellites. The base detection
rate is 1% plus a cumulative 1% per 16 days, and each additional Sensory Matrix
and Subspace Detectors adds another detection attempt per day, although a colony
will never build more than one of each, for a maximum of three chances per day.

Turret
: ![Turret](../images/alien_bldg/axz_turret.gif "turret"){:.left} A plasma turret which deals 5 damage, the same as Terran plasma turrets.
Fires on a 6-day cooldown. The Ax'Zilanths do not use Laser turrets.

Turret
: ![Turret](../images/alien_bldg/axz_turret2.gif "turret"){:.left} A photon turret which deals 8 damage, the same as Terran plasma turrets.
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

To build ships, an Ax'Zilanth colony requires at least one Reactor,
Stabilising Platform, and Engineering Plant. It also requires at least one Ore
Extractor or Resource Podule. They also require at least one Spacecraft Dock,
and produce proportionally faster with up to a maximum of four docks.

Each ship an Armour value, speed, number of hardpoints (sometimes erroneous), ID
number in the game code, chance to build, build time, and up to six hardpoints.
The names here are arbitrary and do not appear in the code.

Name                  | Armour| S | H | ID | Bld%    | Days     | HP1| HP2| HP3| HP4| HP5| HP6|
----------------------|------:|--:|--:|:---|--------:|---------:|----|----|----|----|----|----|
"Fighter"             |    30 | 2 | 2 | 3c | 20%     | 30       | 06 | 09 |    |    |    |    |
"Light Cruiser"       |    40 | 2 | 3 | 3d | 20%     | 35       | 07 | 09 | 01 |    |    |    |
"Heavy Cruiser"       |    40 | 1 | 2 | 3e | &mdash; | &mdash;  | 06 | 05 | 00 | 02 |    |    |
"Scoutship"           |    15 | 1 | 1 | 3f | 10%     | 10       | 06 |    |    |    |    |    |
"Light Bomber"        |    50 | 1 | 4 | 40 | 20%     | 40       | 09 | 07 | 03 | 01 |    |    |
"Heavy Bomber"        |    60 | 1 | 5 | 41 | 20%     | 50       | 09 | 07 | 03 | 01 | 04 |    |
"Transporter"         |    35 | 0 | 2 | 42 |  3%     | 60       | 06 | 06 |    |    |    |    |
"Battleship"          |    90 | 0 | 6 | 43 |  7%     | 90       | 07 | 06 | 03 | 01 | 07 | 03 |
"Orbital Space Dock"  |   200 | 0 | 4 | 4b | ..      | ..       | 06 | 06 | 07 | 0a |    |    |

Ship $3c "Fighter"
: ![axz_ship_small_1](../images/alien_ships/axz_ship_small_1.gif "axz_ship_small_1"){:.left}
A fast 30 Armour ship with a Photon Cannon (8 damage) and Warp Generator.
Warp Generator phases ship out for three days and back in for two. Due to a bug,
however, being phased out has no effect.

Ship $3d "Light Cruiser"
: ![axz_ship_small_2](../images/alien_ships/axz_ship_small_2.gif "axz_ship_small_2"){:.left}
A fast 40 Armour ship with a a Plasma Cannon (5 damage), Warp Generator, and
Disruptor.

Ship $3e ~~"Heavy Cruiser"~~
: ![axz_ship_small_3](../images/alien_ships/axz_ship_small_3.gif "axz_ship_small_3"){:.left}
A slower 40 Armour ship with a Photon Cannon (8 damage), Warp Generator, Ion
Cannon and Disruptor. Listed in the game code has having two hardpoints,
although it has four. Never built randomly.

Ship $3f "Scoutship"
: ![axz_ship_small_4](../images/alien_ships/axz_ship_small_4.gif "axz_ship_small_4"){:.left}
A slower 15 Armour ship with a Photon Cannon (8 damage). The weakest ship. The
Ax'Zilanths and Rigellians are the only two species with a slow scout ship like
this. The only small Ax'Zilanth ship without a Warp Generator.
Each colony sends a scoutship every 130 days, the slowest of any alien.

Ship $40 "Light Bomber"
: ![axz_ship_med_5](../images/alien_ships/axz_ship_med_5.gif "axz_ship_med_5"){:.left}
A slower 50 Armour ship with a Warp Generator, Plasma Cannon (5 damage), Chaos
Bomb and Disruptor.

Ship $41 "Heavy Bomber"
: ![axz_ship_med_6](../images/alien_ships/axz_ship_med_6.gif "axz_ship_med_6"){:.left}
A slower 60 Armour ship with a Warp Generator, Plasma Cannon (5 damage), Chaos
Bomb, Disruptor and Vortex Mine. Identical to the previous ship except for
higher Armour and a Vortex Mine.

Ship $42 "Transporter"
: ![axz_ship_transporter](../images/alien_ships/axz_ship_transporter.gif "axz_ship_transporter"){:.left}
A slow 35 Armour ship with two Photon Cannons (8 damage). A typical
Transporter.

Ship $43 "Battleship"
: ![axz_ship_battleship](../images/alien_ships/axz_ship_battleship.gif "axz_ship_battleship"){:.left}
A slow 90 Armour ship with six hardpoints: two Plasma Cannons (5 damage),
two Chaos Bombs, a Photon Cannon (8 damage) and a Disruptor.

Ship $4b "Orbital Space Dock"
: The first time the colony attempts to spawn a Transporter or Battleship, it
instead creates an Orbital Space Dock. As a result, it effectively has a 10%
build chance and either a 60 or 90 day build time. It is especially strong
compared to other species' OSDs, having 200 Armour instead of 100, plus a
Deflector which effectively doubles that to 400.

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

Each Ax'Zilanth colony considers starting a new colony every 35 days. The
colonization countdown freezes if there is no Strategy Control. The initial
colony takes 80 days to activate, and each new colony takes 40 days to activate.

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

### Population

Population increases by 1 per day, provided that radiation is 40% or lower, and
the colony has at least one Nutrient Podule and Atmospheric Regulator. Radiation
above this amount does not decrease population. Each Personnel Podule has
capacity for 100 population. If there are no Personnel Podules, the colony is
destroyed.

Population decreases by 3 per day without an Atmospheric Regulator, and 1 per
day without a Nutrient Podule. If both are missing, it only loses 1 per day. If
either are missing, it reacts by building an Atmospheric Regulator, Personnel
Podule, Reactor, and Nutrient Podule.

### Spying

Each colony has a daily chance to spot one Terran spy satellite in orbit and
shoot it down. The chance begins at 1% and increases by 1% per 16 days. Once
they shoot a satellite down, the chance drops to 6%.

The daily chance is increased by 1% per 16 days for each Sensory Matrix and
Subspace Detectors.

### Scouting

Every 130 days, each colony sends a scout ship to explore a random sector of
space. This is substantially slower than the others.

### Tactical

The Ax'Zilanths have a very specific military strategy. They have a massive 80
pixel sensor range for detecting incoming missiles (compared to 16 for the Ore
Eaters, for example), but only 30 pixels for detecting incoming fleets.

Every 16th day of the year (days ending in 00, 16, 32, 48, 64, 80, or 96), each
colony measures the damage done to it and retaliates with a missile strike
depending on the amount of damage done since the last check:

- If at least 220 damage, it fires 1-6 Hellfire, 1-3 Nuclear, 1-3 Virus,
  1 Mega, and 1 Stasis
- If at least 150 damage, it fires 1-3 Area Explosive, 1-3 Hellfire,
  1-3 Scatter, 1 Stasis, and 3 Vortex
- If at least 50 damage, it fires 1-3 Hellfire.

Every 8th day that isn't a missile day (days ending in 08, 24, 40, 56, 72,
or 88), it fires a single Static Inducer missile at a random Terran asteroid.

On all other days, there is a 1% chance to trigger the Mass Displacement Podule,
the asteroid teleporter, on a random asteroid. If there is no Mass Displacement
Podule built yet or it doesn't fire, there is a 10 daycolony cycle of proximity
checks for asteroids at risk of collision, where it will immediately attempted
to trigger a teleport. If this isn't possible, its backup plan is to fire one
Mega missile.

If none of these occur, every 8 days divided by number of colonies, it checks
for Terran missiles or spy satellites within sensor range, which is a massive 80
pixel radius; for comparison, that's one quarter of the game screen. It
retaliates by firing 1-4 of a unique missile which deflects incoming missiles.

Failing that, they resort to fleets, but will only use fleets once they have
lost one colony to building destruction (i.e. Terran attack, not asteroid
collision). They need at least 10 ships present to form a fleet, and form fleets
of 0 to 15 ships. The retreat chance is set at 100%; i.e. they will never
retreat until destroyed.
