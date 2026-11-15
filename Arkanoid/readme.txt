Arkanoid and Tournament Arkanoid freeplay and attract mode patches.

These freeplay rom patches work with the original Arkanoid protection MCU.

Arkanoid patch:
---------------

This Arkanoid with freeplay and attract mode patch is based on the
"arkanoidu" roms available in mame. You will need to locate the mame roms,
and then apply the patches in here to them using an IPS patcher:

a75__18.ips to patch the a75__18.ic16 rom
a75__19.ips to patch the a75__19.ic17 rom

Once that is done, they can be burned onto 27256 Eproms and placed in
locations IC17 and IC16.

The patch does the following to the arkanoidu roms:
- Adds freeplay mode (selected with DIP #2)
- Adds cocktail mode (selected with DIP #1)

Tournament Arkanoid patch:
--------------------------

This Tournament Arkanoid with freeplay and attract mode patch is based on
the "arkatour" roms available in mame. You will need to locate the mame
roms, and then apply the patches in here to them:

a75__27.ips to patch the a75__27.ic17 rom
a75__28.ips to patch the a75__28.ic16 rom

Once that is done, they can be burned onto 27256 Eproms and placed in
locations IC17 and IC16.

The patch does the following to the arkatour roms:
- Adds freeplay mode (selected with DIP #2)
- Adds cocktail mode (selected with DIP #1)


DIP Switch settings:
--------------------

These freeplay roms change the meaning of DIP switches #1 and #2, please
see the following table:

                       Arkanoid Freeplay ROM
|--------------------------------------------------------------------|
|    DIP Switch      |  1  |  2  |  3  |  4  |  5  |  6  |  7  |  8  |
|--------------------------------------------------------------------|
| Cabinet: Cocktail  | off |     |     |     |     |     |     |     |
| Cabinet: Upright   | on  |     |     |     |     |     |     |     |
|--------------------------------------------------------------------|
| 1 Coin, 1 Credit   |     | off |     |     |     |     |     |     |
| Freeplay           |     | on  |     |     |     |     |     |     |
|--------------------------------------------------------------------|
|*Number of lives: 3 |     |     | off |     |     |     |     |     |
| Number of lives: 5 |     |     | on  |     |     |     |     |     |
|--------------------------------------------------------------------|
|*Bonus at 20K/60K   |     |     |     | off |     |     |     |     |
| Bonus at 20k only  |     |     |     | on  |     |     |     |     |
|--------------------------------------------------------------------|
|*Difficulty: Easy   |     |     |     |     | off |     |     |     |
| Difficulty: Hard   |     |     |     |     | on  |     |     |     |
|--------------------------------------------------------------------|
|*Test mode: Normal  |     |     |     |     |     | off |     |     |
| Test mode: Test    |     |     |     |     |     | on  |     |     |
|--------------------------------------------------------------------|
|*Screen: Normal     |     |     |     |     |     |     | off |     |
| Screen: Inverted   |     |     |     |     |     |     | on  |     |
|--------------------------------------------------------------------|
| Continued play: No |     |     |     |     |     |     |     | off |
|*Continued play: Yes|     |     |     |     |     |     |     | on  |
|--------------------------------------------------------------------|


Arkanoid bootlegs:
------------------

There are many version of Arkanoid bootlegs. If the bootleg appears to have
an MCU protection chip, the roms in this directory may work. If not, look
in the Arkanoid Bootleg directory in the top level of this repository for
more information.


- mdeslaur

Revision History:
2026-11-15 - Initial version

