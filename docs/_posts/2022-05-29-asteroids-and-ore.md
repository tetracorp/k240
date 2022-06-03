---
layout: post
title: "Asteroids and ore"
categories: game-mechanics
---

There are 24 asteroids in the game, although not all will be in play at any one
time. Each has a unique layout. The game dedicates 750 bytes per asteroid.

1. Table of Contents
{:toc}

### Starting ore

When generated, each asteroid has the following:

| Ore        | Chance | Min |   Max     |
|------------|-------:|----:|----------:|
| Selenium   |    80% | 500 | 100 (898) |
| Asteros    |    80% | 250 | 500       |
| Barium     |    60% | 250 | 500       |
| Crystalite |    80% | 250 | 750       |
| Quazinc    |    70% |  10 | 100       |
| Bytanium   |    50% |  10 | 100       |
| Korellium  |    50% |   1 |  50       |
| Dragonium  |    50% |  10 | 100       |
| Traxium    |    30% |   1 |  10       |
| Nexos      |    20% |   1 |   6       |

"Chance" is the percentage chance of any of this ore being found in the
asteroid. The amount of that ore is a random value between the minimum and
maximum inclusive.

For example, 50% of asteroids contain any Dragonium, and those which do will
have a minimum of 10 and a maximum of 100.

Selenium actually has a maximum of 100, which is less than its minimum of 500.
Due to the way RNG is calculated, this works out to a maximum of 898. See
[Bugs#Selenium calculation bug](../game-mechanics/bugs.html#selenium-calculation-bug)
for the specific formula which causes this.

All asteroids' ore count is generated when the asteroid is generated, which is
either at the beginning of the game, or when it appears mid-game (e.g. to
replace an ateroid destroyed in a collision). It's not determined when you
conduct the ore survey.

### Starting ore (home asteroid)

The exception to this algorithm is your starting asteroid, which always begins
with exactly the following amounts:

| Ore        | Amount |
|------------|-------:|
| Selenium   |   250  |
| Asteros    |   300  |
| Barium     |   300  |
| Crystalite |   100  |
| Quazinc    |    50  |
| Bytanium   |    50  |
| Korellium  |    25  |
| Dragonium  |    28  |
| Traxium    |     0  |
| Nexos      |     0  |

See [income and ore prices](../game-mechanics/income-and-ore-prices.html) for
the ore prices and how they are calculated.

### Asteroid direction and speed

All asteroids spawn with a random speed between 2 and 5.

|Speed| Chance | Chance % |
|:----|-------:|---------:|
|  2  |  6/16  | 37.50%   |
|  3  |  5/16  | 31.25%   |
|  4  |  3/16  | 18.75%   |
|  5  |  4/16  | 25.00%   |

The exceptions are your starting asteroid and the enemy's starting asteroid,
which always begin at zero speed.

There are 24 possible directions.
