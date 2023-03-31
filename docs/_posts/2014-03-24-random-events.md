---
layout: post
title: "Random events"
categories: game-mechanics
---

Random events can occur, such as a solar flare increasing radiation on all
asteroids or a survey discovering more ore deposits than previously thought.

The first random event is always a manual code protection request. It occurs
after 60 days if playing against the first two aliens (Kll-Kp-Qua or Ore
Eaters), or immediately against the later aliens.

Only one manual request is necessary for each time you load the game, even if
you play multiple aliens.  Starting a new game with the Kll-Kp-Qua or Ore Eaters
will reset the wait to 60 days, while starting a new game with another alien
will retain the existing timer.

The next random event after a manual protection code will occur randomly
between 10 and 39 days later. Each random event after that will occur between 60
and 199 days apart.

If you started with the Kll-Kp-Qua or Ore Eaters, your first request (after the
manual protection request) will always be Reinforcements.

If you have no Transporter, the random event is always "The Empire has sent
you a new Transporter". Otherwise, it is chosen at random, with a 1 in 24
chance of each, except for three events which appear twice on the list and
thus have a 2 in 24 chance.

### None

Nothing happens.

### Magnetic Storm

All ships cannot move for 40-198 days.

This also affects missiles and spy satellites in transit.

### Scout Breakup

Goes through all ships until it finds a Scout, then scraps it.

### Radiation Leak

Radiation increases by 10% on one colony. See
[health, radiation and population growth](../game-mechanics/health-radiation-and-population-growth.html)
for the effects of radiation.

### Solar Flare

Radiation increases by 10% on all asteroids, including alien and unoccupied
asteroids. In theory, if the game goes on long enough, you will eventually hit
100% background radiation on all asteroids, although it would take on average
31,080 in-game days or 17.27 unpaused gameplay hours to do this.

### Freak Sensor Scan

Goes through all alien asteroids, starting with the most recent, and reveals the
first undiscovered alien asteroid it finds, awarding a bonus of 10,000 CR. The
Swixaran asteroid cloaking device renders it immune to this effect. You do not
need a Sensor Array to generate a freak sensor scan.

### Survey: More Ore (double chance)

Adds a random amount of every ore to a random asteroid. It never adds Traxium or
Nexos.

| Ore        | Amount |
|------------|--------|
| Selenium   |  0-199 |
| Asteros    |  0-199 |
| Barium     |  0-199 |
| Crystalite |   0-99 |
| Quazinc    |   0-49 |
| Bytanium   |   0-49 |
| Korellium  |   0-19 |
| Dragonium  |    0-9 |

### Survey: Less Ore

Reduces the amount of each ore at a random asteroid by a random amount, to a
minimum of zero. It never reduces Traxium or Nexos. This event can occur at an
asteroid which already has no ore left, but it cannot reduce the ore below zero
and cannot retroactively remove ore that has already been mined.

| Ore        | Amount |
|------------|--------|
| Selenium   |   0-99 |
| Asteros    |   0-99 |
| Barium     |   0-99 |
| Crystalite |   0-49 |
| Quazinc    |   0-24 |
| Bytanium   |   0-24 |
| Korellium  |    0-9 |
| Dragonium  |    0-4 |

This event is ignored if you have only one colony.

### Powerplant Burnout

A Powerplant at a random colony explodes. Radiation increases 10%.

### Gravitational Anomaly

An Asteroid Engine at a random colony explodes. Radiation increases 10%
for some reason, as with Powerplant burnout.

### Pressure Valve Failure

A random colony's air surplus reduces to zero. Only a problem if you don't have
enough Life Support for your population and were relying on surplus air, as lack
of air is instantly fatal to Terrans. The odds of triggering this random event
while under a resource deficiency of air are quite low.

### Ruptured Pipeline

A random colony's water surplus reduces to zero. There's no "food reduces to
zero" event.

### Computer Control Station Failure

A random colony's power surplus reduces to zero.

### Gravitational Vortex

All asteroids change speed and direction.

### Virus Outbreak

If a random colony has insufficient Medical Centres (one for every full 100
colonists after the first 50), the colony suffers a virus outbreak. It loses two
colonists per day until there are enough Medical Centres for the population
level.

### Ore Bribe

You receive 10,000 to 100,000 credits (1 to 10 times 10,000). Your ore shipments
are actually irrelevant: the size of bonus received and your chance of receiving
another bribe are completely random.

### Comet!! (double chance)

A comet appears.

### Reinforcements (double chance)

Receive 5-10 ships randomly chosen from the following types:
Assault Fighter, Combat Eagle, Scoutship, Destructor, Terminator. The ships
are outfitted with random hardpoints, but cannot have Static Inducer or
Warp Generator, and the first hardpoint on each ship is always a weapon.
The ships are sent to a random colony.

### Meteor Shower

A shower of 5-19 meteors is scheduled for a random colony. It behaves like
a missile strike. Meteors deal 30 damage, three times as much as Explosive
missiles, and enough to insta-kill three-quarters of Terran buildings struck
(see [building hitpoints](building-hitpoints.html)).

### Fixed Ore Prices

Between 2 and 5 times, a random ore is fixed in price for 2-5 years each.
If the random number generator picks the same ore more than once, the
duration does not stack.

### New Transporter

Receive a new Transporter. The hardpoints are always random, but cannot include
Static Inducer or Warp Generator. The first hardpoint is always a weapon, which
is why Transporters often seem to arrive with a ridiculous configuration like
two Lasers or a Laser and a Napalm Orb. The transporter is sent to a random
colony.

If you have no Transporter, the random event is always New Transporter.
