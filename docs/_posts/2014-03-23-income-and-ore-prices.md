---
layout: post
title: "Income and Ore Prices"
categories: game-mechanics
---

### Ore prices
Ore prices are recalculated on day 1 of every year. Each ore has a
a random variance which is added to a fixed minimum price
to calculate the current price.

| Ore        | Start   | Minimum |  Variance     | Maximum |
|:-----------|--------:|--------:|--------------:|--------:|
| Selenium   |      50 |      20 |     5 x  0-19 |     115 |
| Asteros    |      80 |      30 |     5 x  0-13 |      95 |
| Barium     |     150 |     100 |     5 x  0-19 |     195 |
| Crystalite |     400 |     200 |    10 x  0-59 |     790 |
| Quazinc    |   1,200 |   1,000 |     5 x  0-99 |   1,495 |
| Bytanium   |   1,300 |   1,000 |     5 x 0-199 |   1,995 |
| Korellium  |   2,300 |   2,000 |    10 x 0-149 |   3,490 |
| Dragonium  |   3,500 |   3,000 |    10 x 0-199 |   4,990 |
| Traxium    |  50,000 |  50,000 |   400 x 0-249 | 149,600 |
| Nexos      | 150,000 | 100,000 | 1,600 x 0-249 | 498,400 |

Start value is recalculated at the beginning of the game, but appears in
the game data and is included here for completeness.

An ore can have its price fixed by the Imperial Treasury for 2-5 years
due to a [random event](random-events.html).
It remains at whatever its current value is
and ignores the next 2-5 recalculation events.

### Alternate income streams
You receive an undocumented income of 100 CR per day for each
asteroid you own, plus 2 CR per day for each colonist. This becomes a
vital source of income in late game.

Certain undocumented events grant valuable bonuses:

- Destroy alien ship #42 (Transporter): 5,000 CR
- Destroy alien ship #43 (Battleship): 10,000 CR
- LOADSADOSH cheat: 100,000 CR

Many events grant useful bonuses:

- Scout reports finding &lt;n&gt; asteroids: 5,000 CR per asteroid
- Sensors discover an asteroid: 5,000 CR
- Sensors discover an alien asteroid: 10,000 CR
- Freak sensor scan discovers alien asteroid: 10,000 CR
- Bribe to improve ore shipments: 10,000 - 100,000 CR
- Destroy alien asteroid: 100,000 CR
