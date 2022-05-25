---
layout: post
title: "Introduction"
categories: game-mechanics
---

When it released in 1994, _K240_ was both criticized and commended for its
complex gameplay. While the concept of a real-time strategy or 4X game is
well-known to players today, it was a relatively new idea back then.

K240 helped players make meaningful choices by providing both on-screen
information windows and a heavy
[game manual](https://www.lemonamiga.com/games/docs.php?id=904) in English,
French, and German, for which the English-language section alone counted over
28,000 words.

However, a significant amount of the game's mechanics were left unexplained, and
even veteran players have difficulty objectively determining the best strategy.
The purpose of this project is to dig deep into the game files and find answers
to the mystery of these undocumented game mechanics. A brief overview is given
below.

### Ships and missiles

We are told how many points of armour each ship has and what each weapon costs
to buy. However, we aren't given any numbers for how much damage each ship
weapon or missile warhead deals.

### Colonies and buildings

Buildings can be damaged by missiles and ship weapons, but we are not given any
details. Discovered features include 
[hit point values](building-hitpoints.html) for all buildings, the effect of
Repair Facility and Building Armour, and a surprising hit point boost for
Protected buildings.

The exact [behaviour](building-behaviour.html) of some buildings is also
ambiguous, such as Turret damage and Anti-Missile Pod hit chance. These have now
been discovered, along with other mechanics such as the order of precedence
under in which buildings fail under power outage, the rate of colonist death due
to red PAFW [resource
deficiency](pafw-and-resource-deficiency.html),
the number of workers required for each building, and some unexpected or
counter-intuitive building effects.

The exact causes and effects of [social unrest](security-and-morale.html) have
been identified.

### Aliens

Alien ships and buildings are even more mysterious. The game leaves us wondering
if aliens follow the same rules as the human player; e.g. requiring ore or
currency to build, susceptibility to radiation, what their building and ship
stats are, and so on.

Several [general alien mechanics](../alien/0-general-alien-mechanics.html) have been
discovered. Additionally, detailed species-specific rules are known for the
[Kll-Kp-Qua](../alien/1-kll-kp-qua.html),
[Lak'Maj'Traal](../alien/2-ore-eaters.html),
[Ax'Zilanths](../alien/3-ax-zilanths.html),
[Tylarans](../alien/4-tylarans.html)
[Rigellians](../alien/5-rigellians.html),
and [Swixarans](../alien/6-swixarans.html), including species-unique missiles
and ship hardpoints.

The exact AI routines of the aliens are reasonably complex, and only partially
known.

### Bugs

Some game mechanics are undocumented because they are unintended; i.e.
[bugs](../game-mechanics/bugs.html).

### Other

Various unexpected events, such as Magnetic Storm, Solar Flare, the appearance
of a comet, or a bribe to increase ore shipments, are in fact completely
[random events](random-events.html).

The rules governing ore price fluctuation, and certain undocumented [income
streams](income-and-ore-prices.html) have been identified.

Various [miscellaneous features](miscellaneous-features.html) have been
discovered. Additionally, twelve [cheat codes](cheats.html) have been
detailed, although these have generally been known since the 1990s.
