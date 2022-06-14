---
layout: post
title: "Health, radiation and population growth"
categories: game-mechanics
---

### Gaining and Losing Colonists

![CPU](../images/buildings/cpu.png "CPU")
{:.right}

Each colony has a 40% chance each day to gain a colonist. This is the
only way to gain workers. Population size does not affect growth rate.

Each colony has a 10% chance per day to lose one colonist. Colonists
can also be lost due to food/air/water shortages, untreated radiation,
virus outbreaks, certain alien bioweapons, desertion during civil unrest,
and sudden housing shortages caused by housing being blown up.
A colony with zero colonists left is automatically destroyed.

### Radiation

![Decontamination Filter](../images/buildings/decontamination_filter.png "Decontamination Filter")
{:.right}

An asteroid's radiation level increases by 10% for every 100 un-mined Asteros,
for every 2 un-mined Traxium, and for every 1 un-mined Nexos. This is why it's
possible to lose or demolish some Decontamination Filters later and remain at 0%
radiation: the ore that was causing part of the radiation has been mined out.
Radiation can also be increased by certain weapons and random events.

Each active Decontamination Filter reduces radiation by 30%.

There is a percentage chance to lose a colonist to radiation sickness
each day, which increases based on the amount of radiation not negated
by Decontamination Filters or treated by Medical Centres. There's an off-by-one
error in the code here which increases the chance by 1%.

Radiation | Chance of losing one colonist
----------|------------------------------
       0% |   1%
      10% |  11%
      20% |  12%
      30% |  14%
      40% |  15%
      50% |  18%
      60% |  21%
      70% |  26%
      80% |  34%
      90% |  51%
     100% | 100%

### Medical Centres

![Medical Centre](../images/buildings/medical_centre.png "Medical Centre")
{:.right}

Medical centres have exactly two uses: to stop virus outbreaks,
and treat radiation sickness.

Each Medical Centre decreases the negative effects of radiation by 10%.
It requires power to do this.

A viral outbreak usually begins due to a
[random event](../game-mechanics/random-events.html). It can also be caused by a
certain Rigellian missile, which causes a blue flash and kills 20 population on
a hit.

Once the colony has one Medical Centre for every 100 colonists after the first
50, the outbreak ends. Otherwise, it loses two colonists per day. This means the
outbreak automatically ends if the population is reduced to 49 or lower.
Medical Centres can end virus outbreaks even if the building is without power.

### Rapidly Declining Population

The "rapidly declining population" warning triggers whenever a colony's
population is 30 or lower.

If there is currently a resource deficiency, the declining population is
attributed to food, water, or air, in that order. If no reason is given, there
may be some other cause, usually high radiation or alien bioweapons.

Note that the population does not need to actually be declining to trigger this
warning, just to be 30 or lower. It can even trigger if the population is
currently increasing, as long as the total is still below 30. This can happen if
you manage to stop the population loss just in time, and your population is now
recovering.

Viral outbreaks can't trigger the rapidly declining population warning on their
own, since outbreaks stop at 49 population, and the warning only triggers at 30.
