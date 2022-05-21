---
layout: post
title: "Powerplant is the worst building"
categories: fun
---

![powerplant](../images/buildings/powerplant.png "powerplant") 
{:.right}

Here I argue that the Powerplant is not only the worst energy generation method
in K240, it's the worst building in the entire game.

1. Table of Contents
{:toc}

### False advertising

First of all, it doesn't even do what it claims.

The Sci-Tek page claims that the Powerplant can produce up to 20 MW/day. It
actually produces 32 MW. (I wondered if this might be a misreading of the code
(decimal 32 = hexadecimal `0x20`), but checking the code it actually just takes
the number of Powerplants and performs an
[arithmetic shift](https://en.wikipedia.org/wiki/Arithmetic_shift) left by five
to multiply it by 32.) The manual gets the value correct, but supposes that it
consumes Asteros at a rate of one per 4 days, and produces 8 MW when Asteros is
depleted.

It doesn't do either of those things.

### The Asteros problem

Asteros does deplete at a rate of one four days, but it does so independently of
the number of Powerplants. Even if you have built no Powerplants, Asteros
depletes on all colonized asteroids at a rate of one unit per four days. You can
test this by establishing a colony without building anything except the C.P.U.
and watching the Asteros deplete over time.

While you have at least one Asteros left un-mined in the asteroid, all
Powerplants generate 32 MW of energy. As soon as you hit zero, they are reduced
to 0 MW. A stipulation of 8 MW per building does indeed occur immediately after
the Powerplant calculation, but it refers to the 8 MW produced by the C.P.U.
Whoever prepared that section in the manual seems to have misread the code.

![mine](../images/buildings/mine.png "mine") 
{:.right}

What makes this worse is that only un-mined Asteros counts. If you have any
Mines, you're directly depleting your source of Powerplant fuel. If you don't
place any Mines at your starting asteroid, the 300 starting Asteros will last
1,200 days or 40 minutes of gameplay minus pauses, maybe an hour including
pauses. You can't transport in Asteros from another asteroid, because Asteros in
stores doesn't count. You're locked in to a limited fuel supply.

You also have to buy the blueprint and wait for it to arrive. The first Imperial
Transport arrives after 150 days, which is your first opportunity to build a
Powerplant, unless you're playing against the Tylarans, which give it to you for
free. It then takes 40 days to finish building the Powerplant.

In testing against the Tylarans, with a single asteroid powered from the
beginning by two Powerplants, and having four Mines chomping away at the
Asteros, the Asteros supply ran out by date E2.386.89, with 135 mined to
storage. In other words, Powerplant will last your first colony under 700 days
under normal circumstances. You now have to replace them with solar tech.

It's also useless at any new asteroid which hasn't got Asteros, such as if you
find a tiny asteroid with mainly rare ores. This is exactly the situation where
you need high-density power generation to save space. If you do get lucky and
find an asteroid particularly rich in Asteros, you will discover that it
generates radiation 10% radiation per 100 Asteros until it's mined.

### Defensibility

In theory, the Powerplant has the most hit points of any power generation
building aside from the C.P.U.:

| Building                       |   Cost  | HP | HP +Armour&dagg; |
|:-------------------------------|--------:|---:|---:|
| C.P.U                          |   8,000 | 36 | 46 |
| Powerplant                     |  10,000 | 34 | 44 |
| Solar Matrix                   |   5,000 | 10 | 20 |
| Protected Solar Matrix         |   7,200 | 20 | 30 |
| Solar Generator                |   1,500 | 10 | 20 |
| Solar Panel                    |     500 |  5 | 15 |

&dagg; Hit points with Building Armour blueprint.

However, this is mitigated by the fact that it's a four-square building.

A single hit with a Nuclear missile (used by all aliens except the Tylarans and
Swixarans) deals 7 damage per building and 9 damage per square, meaning a total
of 16 damage per one-square building and 43 damage to a 2x2 building. The only
power building to survive is Protected Solar Matrix. With the Building Armour
blueprint, Powerplant survives by a single point of damage, but in that
scenario, anything survives except the Solar Panel.

The Rigellians have a more powerful Nuclear which will destroy an armoured
Powerplant, whereas the armoured Solar buildings will still survive this.

### Financial breakdown

Even in the short term, compare to the other default buildings:

| Building                       | Power |  Cost   | Cost/MW |
|:-------------------------------|------:|--------:|--------:|
| Solar Panel                    |  2 MW |    500  |   250   |
| Powerplant                     | 32 MW | 10,000  |   312.5 |
| Solar Generator                |  4 MW |  1,500  |   375   |
| C.P.U                          |  8 MW |  n/a    |   n/a   |

This list is sorted by cost to build divided by megawatts per day power output.
Solar Panel is the cheapest, but would take 16 squares to produce 32 MW.
Powerplant is, initially, cheaper per Megawatt than Solar Generator, which would
take up 8 squares instead of the Powerplant's 4 squares.

However, there's a catch: you have to buy the Powerplant blueprint, at which
point it's only fair to compare it to other power blueprint technology:

- Solar Matrix:      30,000
- Powerplant:        40,000
- Power Amplifier:  100,000

The blueprint for Solar Matrix is 25% cheaper, and it stacks with Power
Amplifier if you buy that later. Power Amplifier, even on its own, is extremely
good because it retroactively upgrades your existing Solar Generators, to the
point where four Solar Generators produces the same energy as a Powerplant in
the same square count for less cost per building. Power Amplifier does not boost
Powerplants.

| Building                       | Power |  Cost   | CD/MW↑| Sq/32MW&ast; |
|:-------------------------------|------:|--------:|------:|----:|
| Solar Panel +Amp               |  4 MW |    500  | 125   |  8  |
| Solar Generator +Amp           |  8 MW |  1,500  | 187.5 |  4  |
| Solar Panel                    |  2 MW |    500  | 250   | 16  |
| Powerplant                     | 32 MW | 10,000  | 312.5 |  4  |
| Solar Matrix +Amp              | 16 MW |  5,000  | 312.5 |  2  |
| Solar Generator                |  4 MW |  1,500  | 375   |  8  |
| Protected Solar Matrix +Amp    | 16 MW |  7,200  | 450   |  2  |
| Solar Matrix                   |  8 MW |  5,000  | 625   |  4  |
| Protected Solar Matrix &dagg;  |  8 MW |  7,200  | 900   |  4  |
| C.P.U                          |  8 MW |  n/a    | n/a   | n/a |

&ast; Squares needed to generate 32 MW.

&dagg; The turret on top of the Protected Solar Matrix is free to power.
Offsetting the usual cost of a Laser Turret and its power usage, it works out to
380 credits per megawatt, or 211 CD/MW with Power Amplifier.

The table above shows the Powerplant to be more cost-effective than anything
except the Solar Panel (which takes up too much space) or buildings with the
benefit of Power Amplifier. However, this is ignoring the price of blueprints.
If you had to buy the blueprint, this has to be factored into the total cost,
becoming most cost-effective over time. The breakdown goes like this:

- At 1 Powerplant, it costs effectively 1,562.50 credits per megawatt, equal to
  an equivalent capacity of Solar Matrices plus its blueprint.
- From 2 to 14 Powerplants, Power is the most cost-effective power generation
  except for Solar Panel and Solar Generator. The only advantage is that
  Powerplant takes up half as much space per Megawatt.
- At 15 Powerplants, it is exactly as cost-effective to purchase the Power
  Amplifier blueprint and build an equivalent capacity of Solar Generators
  (190,000 credits for 480 MW). Solar Generator is thereafter the most
  cost-effective, reaching cost parity with unamplified Solar Generators soon
  thereafter.

### He powerplant too big for he gotdamn asteroid

Suppose we're spamming LOADADOSH [cheats](../game-mechanics/cheats.html) and
money is no object. In terms of space efficiency, Powerplant is still inferior.
Suppose we build four squares of each power building:

| Building                       | Pow x4↓| Cost x4↑ |
|:-------------------------------|-------:|---------:|
| Solar Matrix +Amp              |  64 MW |   20,000 |
| Protected Solar Matrix +Amp    |  64 MW |   28,800 |
| Solar Generator +Amp           |  32 MW |    6,000 |
| Powerplant                     |  32 MW |   10,000 |
| Solar Matrix                   |  32 MW |   20,000 |
| Protected Solar Matrix&dagg;   |  32 MW |   28,800 |
| Solar Generator                |  16 MW |    6,000 |
| Solar Panel +Amp               |  16 MW |    2,000 |
| Solar Panel                    |   8 MW |    2,000 |
| C.P.U                          |   8 MW |      n/a |

The Power Amplifier blueprint is really the killer app of solar tech.

With the Power Amplifier blueprint, four Solar Generators produce the same
amount of energy as a Powerplant and take up the same space. Effectively, once
you buy it, all your existing Solar Generators now have the energy density of
Powerplants, and for less money. In the late game, this allows you the capacity
to power a lot more Resiblocks and such as an income stream, convert old mining
colonies into shipyards, and so on. At this point, Powerplants in your early
colonies would simply be failing, and you'd need to replace them with Solar
Generators anyway.

There are also two buildings with greater energy density than the Powerplant:
the amplified Solar Matrix and Protected Solar Matrix, allowing you to run an
entire colony from a single square power building.

### Huge fake plastic gun on the top

![protected_solar_matrix](../images/buildings/protected_solar_matrix.png "protected_solar_matrix") 
{:.right}

The Protected Solar Matrix also does something the Powerplant can't, which is to
have a laser turret on top. The additional price makes it the most expensive
building, but it's actually cheaper than building a Solar Matrix plus a separate
Laser Turret. Effectively, you get the Solar Matrix component for only 3,800
credits.

Even without Power Amplifier, 4x Protected Solar Matrix brings four Laser
Turrets, each of which is firing for 2 damage on a 5 day cooldown. Turret
Optimizer also applies to Protected buildings, making each of those a 4 damage
Turret. (Note that turrets on Protected buildings still fail when Laser Turret
would fail due to power shortage.) The Protected Solar Matrix also has improved
hit points.

Additionally, the turret is powered for free, saving you +2 power. Effectively,
it's generating 10 MW unamplified for 3,800 (380 CD/MW), or 18 MW amplified for
3,800 (211.11 CD/MW).

Factoring for the Laser Turret, then, the Protected Solar Matrix is the
champion. Unamplified, the PSM is more cost-effective per unit until we build 6
Powerplants. With the Power Amplifier, however, PSM becomes cheaper from the
equivalent of 2 Powerplants onward, and remains massively cost-effective. From
about 192 MW capacity (12 buildings), PSM becomes even more cost-effective than
base Solar Generator, and at 800 MW capacity onward (50 buildings), PSM actually
becomes more cost-effective than base Solar Panels.

### Dangers of nuclear power

There's also a [random event](../game-mechanics/random-events.html) which causes
a Powerplant Burnout. A random Powerplant explodes, causing radiation at that
asteroid to increase by 10%. It's similar to the Gravitational Anomaly which
destroys Asteroid Engines, a more common occurrence since people actually build
Asteroid Engines.

When it explodes, you also lose 32 MW of power generation, so now you're
struggling to build power in the middle of a power shortage.

### Summary

The Powerplant is a terrible building. It's big, expensive, requires a
blueprint, runs out of fuel within 700 days, and won't work some asteroids. It's
especially vulnerable to nuclear attack, and only works on asteroids prone to
high radiation in the first place. Its only advantage over plain Solar
Generators is energy density per square, and it's not even the best at that.
Finally, there's a random chance that it'll just explode.

The smart alternative is just to build Solar Generators until you can buy Power
Amplifier, at which point there is no reason at all to build Powerplants because
Solar Generators will do the same job in the same space for substantially less
money. Powerplant is a terrible building because not only is it bad, you have to
pay for it, and then it stops working.
