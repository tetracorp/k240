---
layout: post
title: "Save game format"
categories: data
---

K240 can store up to four save game files, stored as `k240.1", `k240.2",
`k240.3", and `k240.4". If the game has been installed to hard disk, these games
are loaded from the game install directory. Otherwise, they are loaded from
`DF0:`. The game determines whether it's running from a HD install by checking
for a file called `k240_2:idfile`, which appears on the disk 2 but is
intentionally omitted from the hard disk install.

Each save game file is 151,850 bytes.

### Overview

| Offset  | Length | Description |
|--------:|-------:|-------------|
|       0 |     18 | Save game name (16 bytes) and current alien ID (2 bytes). |
|      18 |     30 | Alien variables (`a1data{1-6}.bin` +4 bytes, for 30 bytes). |
|      48 | 55,810 | Miscellaneous game state: Transporter cargo, extracted buttons, asteroid maps (53,856 bytes for 24 asteroids at 34x33 words each), current money, Imperial transporter timer, asteroid hotkeys, comet locations, blueprints owned, date, numerous others. |
|  55,858 | 37,800 | Ships. 700 ships at 54 bytes per ship. "Ships" includes missiles, satellites, and Vortex storms. |
|  93,658 | 33,600 | Buildings. 14 bytes per building, 100 buildings per asteroid, 24 asteroids. |
| 127,258 | 18,000 | Asteroids. 24 asteroids at 750 bytes each. |
| 145,258 |  1,920 | Building totals. 24 asteroids, 80 buildings per asteroid (40 Terran, 40 alien) |
| 147,178 |  2,336 | Terran fleets. |
| 149,514 |  2,336 | Alien fleets.  |
|         |151,850 | TOTAL |

### Save name (18 bytes)

| Length | Description |
|-------:|-------------|
|     16 | Save name typed in by the user |
|      2 | Alien ID (1-6) |

### Alien variables (30 bytes)

Consists of variables specific to the current alien. These are loaded from the
alien file `a1data1.bin` to `a1data6.bin` depending on alien. The first four
bytes of that file are a pointer, and the next 30 bytes are copied to this save
game section. Most are read-only and do not change.

| Length | Description |
|-------:|-------------|
|      2 | Alien ID number (1-6). |
|      2 | Days between new building clusters. 70 for Tylaran, 50 for Swixaran, 60 for all others. |
|      2 | Build timer. Increments by 1 daily and resets when it hits the build number. |
|      2 | Scout frequency. Kll 70, Ore 30, Axz 130, Tyl 40, Rig 50, Swi 40 |
|      2 | New colony frequency. Kll 200, Ore 30, Axz 35, Tyl 45, Rig 35, Swi 120 |
|      2 | Missile build frequency. Kll 25, Ore 35, Axz 30, Tyl 0, Rig 30, Swi 30 |
|      2 | Percentage chance to ignore building softcap. Kll 20, Ore 10, Axz 15, Tyl 15, Rig 25, Swi 25 |
|      2 | Missile freq (unknown). Ore 200, Tyl 100, others 0. Can be set to 100, decremented, compared to 140 |
|      2 | Missile countdown. Rigellian starts at 100, others at 0. Loops 80-0. |
|      2 | Laser damage. Kll 2, Ore 2, Axz 3, Tyl 4, Rig 5, Swi 0 |
|      2 | Plasma damage. Kll 4, Ore 4, Axz 5, Tyl 6, Rig 7, Swi 7 |
|      2 | Photon damage. Kll 6, Ore 6, Axz 8, Tyl 10, Rig 0 |
|      2 | Missile (range/chance?). Kll 16, Ore 16, Axz 80, Tyl 0 Rig 40, Swi 30 |
|      2 | Missile (?). Kll 40, Ore 40, Axz 30, Tyl 0, Rig 30, Swi 20 |
|      1 | Turret cooldown. Kll 8, Ore 6, Axz 6, Tyl 6, Rig 6, Swi 5 |
|      1 | Bitfield. Bit 4: Swixaran asteroid cloak active. |

### Main game state (55,810 bytes)

A large section of memory which holds a variety of variables which store the
game state. Represented in the v2.000 executable as `$20a8c` to `$2e48e`. Most
of this is the asteroid maps. Offsets here are given from the location in the
executable file rather than the section. Variables with generic names are as yet
undiscovered in purpose. You can read more detail in the commented source file,
which has more comments and may have a more up to date explanation.

Of particular notice are:
- Transporters, which max out at 10; the cargo holds appear later, and include
  an eleventh cargo hold to represent the Imperial Transporter
- Ore price charts
- Building keybinds for pressing 0-9
- Extracted button locations
- Asteroid maps, 24 asteroids, each 34x33 of two-byte tiles, where the second
  byte is the sprite number
- Blueprints flags
- Game clock
- An alien special bitfield, tracking three things:
  - Bit 0: Set when Ax'zilanth first hit by a Virus missile; subsequent Virus
    missiles will fail because they have adapted
  - Bit 1: Set when Ax'zilanth loses a colony to housing destruction, presumably
    triggering retaliation or a special state of war
  - Bit 2: Set by default, cleared when both Swixaran cloaks are down

| Offset   | Length | Description |
|:---------|-------:|-------------|
| `$20a8c` | 80 | tblTransporters |
| `$20adc` | 16 | tblOrePrice0Sel |
| `$20aec` | 16 | tblOrePrice1Ast |
| `$20afc` | 16 | tblOrePrice2Bar |
| `$20b0c` | 16 | tblOrePrice3Cry |
| `$20b1c` | 16 | tblOrePrice4Qua |
| `$20b2c` | 16 | tblOrePrice5Byt |
| `$20b3c` | 16 | tblOrePrice6Kor |
| `$20b4c` | 16 | tblOrePrice7Dra |
| `$20b5c` | 16 | tblOrePrice8Tra |
| `$20b6c` | 16 | tblOrePrice9Nex |
| `$20b7c` | 20 | arrBlueButtonBldgs |
| `$20b90` | 6 | arrButton0 |
| `$20b96` | 6 | arrButton1 |
| `$20b9c` | 78 | arrButton2 |
| `$20bea` | 2 | padding_20bea |
| `$20bec` | 53,856 | tblAsteroidMaps |
| `$2de4c` | 4 | ptrAsteroids2de4c |
| `$2de50` | 4 | lAstUnknown52 |
| `$2de54` | 4 | lUnknown53 |
| `$2de58` | 4 | ptrCurrentAst |
| `$2de5c` | 4 | lUnknownSat54 |
| `$2de60` | 4 | ptrEnemyHome |
| `$2de64` | 4 | ptrHomeAst |
| `$2de68` | 4 | intCashGeneral |
| `$2de6c` | 4 | intCashBuilding |
| `$2de70` | 4 | intCashVehicles |
| `$2de74` | 4 | intCashIntel |
| `$2de78` | 4 | intCashMissiles |
| `$2de7c` | 4 | ptrAstTarget |
| `$2de80` | 4 | ptrAst2DE80 |
| `$2de84` | 4 | ptrImpTransport |
| `$2de88` | 40 | arrHotkeys |
| `$2deb0` | 4 | ptr2DEB0 |
| `$2deb4` | 4 | ptr2DEB4 |
| `$2deb8` | 4 | ptr2DEB8 |
| `$2debc` | 4 | data2DEBC |
| `$2dec0` | 4 | data2DEC0 |
| `$2dec4` | 4 | ptrFleet_2DEC4 |
| `$2dec8` | 4 | ptr2DEC8 |
| `$2decc` | 4 | ptrThisAstMap |
| `$2ded0` | 4 | ptrThisAstBldg |
| `$2ded4` | 4 | ptrThisAstBldgCount |
| `$2ded8` | 4 | ptrThisAstStats |
| `$2dedc` | 4 | ptrShips_2DEDC |
| `$2dee0` | 4 | ptr2DEE0 |
| `$2dee4` | 4 | ptr2DEE4 |
| `$2dee8` | 4 | ptr2DEE8 |
| `$2deec` | 4 | ptrAstMap_2DEEC |
| `$2def0` | 4 | ptrAstBldg_2DEF0 |
| `$2def4` | 4 | ptrBldCount_2DEF4 |
| `$2def8` | 4 | ptr2DEF8 |
| `$2defc` | 2 | intOutroMsg |
| `$2defe` | 4 | ptrOutroImg |
| `$2df02` | 2 | intCurrentAlienID |
| `$2df04` | 1 | flgUnknown61 |
| `$2df05` | 1 | intAlienColonies |
| `$2df06` | 256 | ptr2DF06 |
| `$2e006` | 4 | ptr2E006 |
| `$2e00a` | 2 | astCount |
| `$2e00c` | 1 | intAstUnknown63 |
| `$2e00d` | 1 | flgUnknown64 |
| `$2e00e` | 1 | flg2E00E |
| `$2e00f` | 3 | info_display |
| `$2e012` | 64 | ptr2E012 |
| `$2e052` | 2 | intOurAstsKnown |
| `$2e054` | 2 | intOurAstsKnownUnused |
| `$2e056` | 2 | intAlienAstCount |
| `$2e058` | 2 | intImpTransport |
| `$2e05a` | 2 | intImpLeaveTimer |
| `$2e05c` | 44 | ptr2E05C |
| `$2e088` | 2 | currBlueBuild |
| `$2e08a` | 2 | data2E08A |
| `$2e08c` | 2 | data2E08C |
| `$2e08e` | 2 | data2E08E |
| `$2e090` | 6 | dataAst2E090 |
| `$2e096` | 2 | intCometHoriz |
| `$2e098` | 2 | intCometVert |
| `$2e09a` | 1 | data2E09A |
| `$2e09b` | 1 | flg2E09B |
| `$2e09c` | 1 | flg2E09C |
| `$2e09d` | 1 | flg2E09D |
| `$2e09e` | 1 | flg2E09E |
| `$2e09f` | 1 | flgScreen2E09F |
| `$2e0a0` | 1 | flg2E0A0 |
| `$2e0a1` | 1 | flg2E0A1 |
| `$2e0a2` | 2 | intTotalShips |
| `$2e0a4` | 2 | data2E0A4 |
| `$2e0a6` | 2 | data2E0A6 |
| `$2e0a8` | 2 | screenFlashColor |
| `$2e0aa` | 2 | intTotalCommandCen |
| `$2e0ac` | 20 | arrCargo00 |
| `$2e0c0` | 20 | arrCargo01 |
| `$2e0d4` | 20 | arrCargo02 |
| `$2e0e8` | 20 | arrCargo03 |
| `$2e0fc` | 20 | arrCargo04 |
| `$2e110` | 20 | arrCargo05 |
| `$2e124` | 20 | arrCargo06 |
| `$2e138` | 20 | arrCargo07 |
| `$2e14c` | 20 | arrCargo08 |
| `$2e160` | 20 | arrCargo09 |
| `$2e174` | 20 | arrCargoImp |
| `$2e188` | 1 | flgAst2E188 |
| `$2e189` | 1 | flgAst2E189 |
| `$2e18a` | 640 | tblShipyards |
| `$2e40a` | 1 | ptr2E40A |
| `$2e40b` | 34 | ptr2E40B |
| `$2e42d` | 1 | flg2E42D |
| `$2e42e` | 1 | flgBP2GMine |
| `$2e42f` | 1 | flgBP2GDeepMine |
| `$2e430` | 1 | flgBPAntiMissilePod |
| `$2e431` | 1 | flgBPAntivirusMissile |
| `$2e432` | 1 | flgBPAsteroidEngines |
| `$2e433` | 1 | flgBPAstTracker |
| `$2e434` | 1 | flgBPBldgArmor |
| `$2e435` | 1 | flgBPConstrDroids |
| `$2e436` | 1 | flgBPDeflector |
| `$2e437` | 1 | flgBPFBattleship |
| `$2e438` | 1 | flgBPGravityNullifier |
| `$2e439` | 1 | flgBPHiPowerStore |
| `$2e43a` | 1 | flgBPImpSensors |
| `$2e43b` | 1 | flgBPMegaMissile |
| `$2e43c` | 1 | flgBPMislBayExt |
| `$2e43d` | 1 | flgBPMislGuidance |
| `$2e43e` | 1 | flgBPNuclearMissile |
| `$2e43f` | 1 | flgBPOreTeleporter |
| `$2e440` | 1 | flgBPPhotonTurret |
| `$2e441` | 1 | flgBPPlasmaTurret |
| `$2e442` | 1 | flgBPPowerAmplifier |
| `$2e443` | 1 | flgBPPowerplant |
| `$2e444` | 1 | flgBPRepairFacility |
| `$2e445` | 1 | flgBPScreenGenerator |
| `$2e446` | 1 | flgBPSeismicPenetrator |
| `$2e447` | 1 | flgBPShield40 |
| `$2e448` | 1 | flgBPShield50 |
| `$2e449` | 1 | flgBPSolarMatrix |
| `$2e44a` | 1 | flgBPStaticInducer |
| `$2e44b` | 1 | flgBPStasisMissile |
| `$2e44c` | 1 | flgBPTerminator |
| `$2e44d` | 1 | flgBPTurretOpt |
| `$2e44e` | 1 | flgBPVirusMissile |
| `$2e44f` | 1 | flgBPWarpGen |
| `$2e450` | 1 | flgSoundEnabled |
| `$2e451` | 1 | flgVoice |
| `$2e452` | 1 | intEventCountdown |
| `$2e453` | 1 | intNextEvent |
| `$2e454` | 1 | intMagStorm |
| `$2e455` | 1 | int2E455 |
| `$2e456` | 1 | intMeteorCountd |
| `$2e457` | 1 | popWarnTimer |
| `$2e458` | 1 | flgPaused |
| `$2e459` | 1 | flg2E459 |
| `$2e45a` | 1 | bFrameRule |
| `$2e45b` | 1 | intDay |
| `$2e45c` | 2 | intClockYear |
| `$2e45e` | 8 | strClock |
| `$2e466` | 2 | ptr2E466 |
| `$2e468` | 1 | flgShowGfx |
| `$2e469` | 1 | flg2E469 |
| `$2e46a` | 1 | flg2E46A |
| `$2e46b` | 1 | flg2E46B |
| `$2e46c` | 1 | flg2E46C |
| `$2e46d` | 1 | flgShipActive_2E46D |
| `$2e46e` | 1 | flgDSound1 |
| `$2e46f` | 1 | flgDSound2 |
| `$2e470` | 1 | int2E470 |
| `$2e471` | 1 | int2E471 |
| `$2e472` | 1 | int2E472 |
| `$2e473` | 1 | int2E473 |
| `$2e474` | 1 | flgStatic2E474 |
| `$2e475` | 1 | flg2E475 |
| `$2e476` | 1 | textcolor |
| `$2e477` | 1 | tmpTextcolor |
| `$2e478` | 1 | flg2E478 |
| `$2e479` | 1 | flg2E479 |
| `$2e47a` | 1 | flg2E47A |
| `$2e47b` | 1 | flg2E47B |
| `$2e47c` | 1 | flg2E47C |
| `$2e47d` | 1 | flg2E47D |
| `$2e47e` | 1 | flg2E47E |
| `$2e47f` | 1 | flg2E47F |
| `$2e480` | 1 | flg2E480 |
| `$2e481` | 1 | flg2E481 |
| `$2e482` | 1 | flg2E482 |
| `$2e483` | 1 | flg2E483 |
| `$2e484` | 2 | intAsteroidFacing |
| `$2e486` | 1 | intScreen |
| `$2e487` | 1 | intPrevScreen |
| `$2e488` | 1 | intNewScreen |
| `$2e489` | 1 | flg2E489 |
| `$2e48a` | 1 | flgShowUI |
| `$2e48b` | 1 | flgRedraw |
| `$2e48c` | 1 | intPointer |
| `$2e48d` | 1 | bAlienSpecial |

### Ships (37,800 bytes)

700 ships, 54 bytes per ship. "Ship" in this case means any movable sprite,
including missiles, satellites en route, fire, and vortex storms. The following
is the format for the ship data structure. (Not fully discovered yet.)

|Offset|Length| Description            |
|-----:|-----:|------------------------|
|    0 |    4 |                        |
|    4 |    4 |                        |
|    8 |    1 | ShipID                 |
|    9 |    1 | Facing                 |
|   10 |    1 | coord_x                |
|   11 |    1 | coord_y                |
|   12 |    1 | Position??             |
|   13 |    1 |                        |
|   14 |    2 |                        |
|   16 |    1 |                        |
|   17 |    1 |                        |
|   18 |    1 | frame                  |
|   19 |    1 | anim?                  |
| 20b6 |  bit |                        |
| 20b5 |  bit |                        |
| 20b4 |  bit | MissionComplete?       |
| 20b3 |  bit | Large                  |
| 20b2 |  bit |                        |
| 20b1 |  bit | osd                    |
| 20b0 |  bit | Speed                  |
| 21b7 |  bit | Owner                  |
| 21b6 |  bit | Firing Weapon          |
| 21b5 |  bit | Deflector              |
| 21b4 |  bit | ship??                 |
| 21b3 |  bit | Missile launch         |
| 21b2 |  bit | Static Inducer?        |
| 21b1 |  bit | Warp Generator         |
| 21b0 |  bit | 0 unknown              |
|   22 |    1 | Cooldown               |
|   23 |    1 | bitfield23?            |
|   24 |    1 | Action                 |
|   25 |    1 | Action2                |
|   26 |    1 | Pop?IntelBldg          |
|   27 |    1 | Warhead_IntelShips     |
|   28 |    4 | Target?                |
|   32 |    1 | Origin                 |
|   33 |    1 | Destination            |
|   34 |    1 | AstDiscovered          |
|   35 |    1 | IntelShipsBig          |
|   36 |    2 | Alive                  |
|   38 |    2 | Position?              |
|   40 |    2 |                        |
|   42 |    6 | Hardpoints             |
|   48 |    1 | FleetID                |
|   49 |    1 | Self-destruct timer    |
|   50 |    2 | Armour                 |
|   52 |    1 | Warp generator timer   |
|   53 |    1 | padding?               |

### Buildings (33,600 bytes)

24 asteroids, 100 buildings per asteroid, 14 bytes per building.

| Offset | Length | Name                           | 
|--------|--------|--------------------------------|
| 0      | 1      | BuildingID                     | 
| 1      | 1      | Hitpoints                      | 
| 2      | 1      | DaysToBuild                    | 
| 3      | 1      |                                | 
| 4      | 1      | CoordX                         | 
| 5      | 1      | CoordY (bit7=shield generator) |
| 6      | 6      | 4sqCoords/anim                 | 
| 12     | 1      | Cooldown/YardID                | 
| 13     | 1      |                                | 

### Asteroids (18,000 bytes)

24 asteroids, 750 bytes per asteroid. (Not fully discovered yet.)

| Offset | Length | Name                          | 
|--------|--------|-------------------------------|
| 0      | 4      | ptr0                          | 
| 4      | 4      | ?4                            | 
| 8      | 4      | ShipBuild                     | 
| 12     | 4      | ?12                           | 
| 16     | 4      | missiles2?                    | 
| 20     | 1      |                               | 
| 21     | 1      | Visible                       | 
| 22     | 1      |                               | 
| 23     | 1      |                               | 
| 24     | 1      | Speed                         | 
| 25     | 1      | Exists                        | 
| 26     | 2      | coord_x                       | 
| 28     | 2      | coord_y                       | 
| 30     | 1      |                               | 
| 31     | 1      |                               | 
| 32     | 1      |                               | 
| 33     | 1      |                               | 
| 34     | 1      |                               | 
| 35     | 1      | movement?                     | 
| 36     | 1      |                               | 
| 37     | 1      |                               | 
| 38     | 1      |                               | 
| 39     | 1      |                               | 
| 40     | 16     | Name                          | 
| 56     | 2      | direction1                    | 
| 58     | 2      | direction2                    | 
| 60     | 20     | Ore                           | 
| 80     | 1      | Radiation                     | 
| 81     | 1      | Background radiation          | 
| 82     | 2      | Damage                        | 
| 84     | 2      | Unrest                        | 
| 86     | 1      | Security present              | 
| 87     | 1      | Strike duration               | 
| 88     | 1      | Anti-Missile Pods x2          | 
| 89b7   | bit    | Stasis                        | 
| 89b6   | bit    | Player Can't Build            |
| 89b5   | bit    | Ore Surveyed                  | 
| 89b4   | bit    | Known to Player               | 
| 89b3   | bit    | Engine Active                 | 
| 89b2   | bit    | Gravity Nullifier Active      | 
| 89b1   | bit    | Viewable to Player            |
| 89b0   | bit    | Occupied                      |
| 90b7   | bit    | Virused                       |
| 90b6   | bit    | OreEater boobytrap            | 
| 90b5   | bit    | Screen Generator recalc       | 
| 90b4   | bit    | OSD                           | 
| 90b3   | bit    | Known to enemy?               |
| 90b2   | bit    | Outbreak                      | 
| 90b1   | bit    | b90-1                         |
| 90b0   | bit    | OreEatClr0                    |
| 91b7   | bit    |                               | 
| 91b6   | bit    |                               | 
| 91b5   | bit    |                               | 
| 91b4   | bit    | Swi-detectedSpy               | 
| 91b3   | bit    | Missl?                        | 
| 91b2   | bit    |                               | 
| 91b1   | bit    | Outpost (founded by Tyl small transporter) |
| 91b0   | bit    | no missile?                   | 
| 92b3   | bit    | Worker shortage: Missile construction | 
| 92b2   | bit    | Worker shortage: Shipyard     | 
| 92b1   | bit    | Worker shortage: Deep Bore/Seismic  | 
| 92b0   | bit    | Worker shortage: Mine         | 
| 93     | 1      |                               | 
| 94     | 1      |                               | 
| 95     | 1      |                               | 
| 96     | 1      | Satellites orbiting           | 
| 97     | 1      | Satellite spot chance         | 
| 98     | 1      |                               | 
| 99     | 1      |                               | 
| 100    | 22     | Missiles in silo              | 
| 122    | 22     | Missiles launching            | 
| 144    | 22     | Missile build queue           | 
| 166    | 2      | Total launching               | 
| 168    | 1      | Sattelites in silo?           | 
| 169    | 1      | Satellites launching?         | 
| 170    | 1      | Satellite build queue         | 
| 171    | 1      |                               | 
| 172    | 1      | hits                          |
| 173    | 1      |                               | 
| 174    | 4      |                               | 
| 178    | 4      | Missile target                | 
| 182    | 20     | Ore in stores                 | 
| 202    | 2      | Total ore in stores           | 
| 204-683| 497    | UNKNOWN                       | 
| 684    | 2      | Population                    | 
| 686    | 1      |                               | 
| 687    | 1      |                               | 
| 688    | 1      |                               | 
| 689    | 1      |                               | 
| 690    | 1      |                               | 
| 691    | 1      |                               | 
| 692    | 2      | CPU production (Alien starts at 40        |
| 694    | 2      | Power production                          | 
| 696    | 2      | Power usage / Alien scout freq            |
| 698    | 2      | Power surplus / Alien new col freq        |
| 700    | 2      | Air production / Alien missile build freq |
| 702    | 2      | Air usage / Alien shipbuilding            |
| 704    | 2      | Air surplus                               | 
| 706    | 2      | Food production                           | 
| 708    | 2      | Food usage                                | 
| 710    | 2      | Food surplus / Tyl energiser countdown    |
| 712    | 2      | Water production                          | 
| 714    | 2      | Water usage                               | 
| 716    | 2      | Water surplus                             | 
| 718    | 2      | Power outage                              | 
| 720    | 2      | Worker surplus / Alien build priority     |
| 722    | 2      | CPU air                       | 
| 724    | 2      | CPU food                      | 
| 726    | 2      | CPU water                     | 
| 728    | 2      | Intel missile destination     | 
| 730    | 4      | Intel fleet destination       | 
| 734    | 1      | Shipyard: ships left          | 
| 735    | 1      | Shipyard: ShipID              | 
| 736    | 6      | Shipyard: Hardpoints          | 
| 742    | 1      | Shipyard: Days left           | 
| 743    | 1      | Shipyard: Ore1 needed         | 
| 744    | 1      | Shipyard: Ore2 needed         | 
| 745    | 1      | Shipyard: Ship size           | 
| 746    | 4      | Shipyard: addr?               | 

### Building totals (1,920 bytes)

24 asteroids, 80 building totals per asteroid (40 Terran, 40 alien).

### Terran fleets (2,336 bytes)

8 fleets, 292 bytes per fleet.

| Offset | Length | Name                      | 
|--------|--------|---------------------------|
| 0      | 1      | id?                       |       
| 1      | 1      |                           |       
| 2      | 2      |                           |       
| 4      | 2      |                           |       
| 6      | 4      | Location                  |       
| 10     | 4      | Destination               |       
| 14     | 1      |                           |       
| 15     | 1      |                           |       
| 16     | 1      |                           |       
| 17     | 1      |                           |       
| 18     | 1      |                           |       
| 19     | 1      |                           |       
| 20     | 1      |                           |       
| 21     | 1      |                           |       
| 22     | 2      | ghost? 5555 = ghost fleet | 
| 24     | 2      | 70, 40 tyl                | 
| 26     | 1      |                           |       
| 27     | 1      | spaces?                   |       
| 28     | 1      |                           |       
| 29     | 1      |                           |       
| 30     | 2      | alien?                    |       
| 32     | 256    | ships (64 ptrs)           |       
| 288    | 1      |                           |       
| 289    | 1      |                           |       
| 290    | 1      |                           |       
| 291    | 1      |                           |       

### Alien fleets (2,336 bytes)

Same as Terran fleets.
