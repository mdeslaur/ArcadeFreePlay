Arkanoid and Tournament Arkanoid freeplay and attract mode patches.

Arkanoid patch:
---------------

This Arkanoid with freeplay and attract mode patch is based on the
"arkatayt" bootleg roms available in mame. You will need to locate the
mame roms, and then apply the patches in here to them:

xdelta3.exe -d -s old\ic81-v.3f Arkanoid\ic81_freeplay.patch new\ic81-v.3f
xdelta3.exe -d -s old\ic82-w.5f Arkanoid\ic82_freeplay.patch new\ic82-w.5f

Once that is done, they can be burned onto 27256 Eproms and placed in
locations IC17 and IC16. The ic81-v.3f rom goes into location IC17, and the
ic82-w.5f rom goes into location IC16.

The patch does the following to the arkatayt roms:
- Adds freeplay mode (selected with DIP #2)
- Removes the "WAIT" screen at boot
- Fixes the corruption in the bricks on levels 16 and 25
- Restores the original copyright notice

Tournament Arkanoid patch:
--------------------------

This Tournament Arkanoid with freeplay and attract mode patch is based on
the "arkatour" roms available in mame. You will need to locate the mame
roms, and then apply the patches in here to them:

xdelta3.exe -d -s old\a75-28.ic16 Tournament\ic16_freeplay.patch new\a75-28.ic16
xdelta3.exe -d -s old\a75-27.ic17 Tournament\ic17_freeplay.patch new\a75-27.ic17

Once that is done, they can be burned onto 27256 Eproms and placed in
locations IC17 and IC16.

The patch does the following to the arkatour roms:
- Adds freeplay mode (selected with DIP #2)
- Adds cocktail mode (selected with DIP #1)
- Bypasses the MPU protection


For bootleg Arkanoid PCBs with no MCU:
--------------------------------------

This should be a simple ROM swap. I've tested it with a couple of different
bootleg boards, including some that used the arkangc2 roms, and it worked
without issue.

There are a whole slew of different bootleg boards out there, so this may
not be the case for every one of them. Also, this rom image doesn't have a
level select option, which some bootlegs have.

Please keep in mind that the IC numbers on bootleg boards usually don't
match up to the IC numbers on a real Taito board, so use the layout in the
Arkanoid schematics to figure out where the ICs are located. In general
though, IC81 = IC17 and IC82 = IC16.


For original Taito Arkanoid PCBs:
---------------------------------

Original Taito Arkanoid PCBs use an MCU as protection to prevent the roms
from being modified. This is why a bootleg rom set was chosen as the
starting point for the Arkanoid patch, as all the MCU checks have already
been bypassed. For the Tournament Arkanoid roms, the MCU checks have been
bypassed.

Unfortunately, a modification needs to be done to the original Taito PCB to
be able to run thise romsets:

- The MCU chip at IC14 needs to be removed and a socket with jumpers needs
  to be fitted in its place. The pinouts for the jumpers are as follows:
  - Pin  7 to pin 11
  - Pin 12 to pin 20
  - Pin 13 to pin 21
  - Pin 14 to pin 22
  - Pin 15 to pin 23
  - Pin 16 to pin 24
  - Pin 17 to pin 25
  - Pin 18 to pin 26
  - Pin 19 to pin 27

This modification can be seen in the before.jpg and after.jpg images
included in this zip.

Alternatively, I have designed a small pcb that can be ordered from a PCB
fabrication company that can take the place of the MCU without requiring
to solder jumpers. It can be found here:

https://github.com/mdeslaur/arkanoid-mpu-bypass (the gerbers are available
in the gerbers/amb-gerbers.zip file)

This modification should be easily reversible if something goes wrong or
doesn't work, but please remember that modifying your PCB is at your own
risk. I am not responsible if something goes wrong, your PCB breaks, and
you spend the rest of your life trembling and miserable in the fetal
position longing for the good old days when you could play Arkanoid.

Please keep the original MCU chip with the original PCB in case someone
wants to undo the modification in the future.

While modifying a Taito PCB is annoying, doing so will allow:
- This cool freeplay mod on dipswitch #2.
- Cocktail mode on dipswitch #1, which a lot of original Taito boards don't
  have enabled.
- The possibility of installing Tournament Arkanoid without needing a new
  MCU. (Though it does require new graphics roms, and 3 new colour proms)
- The possibility of installing a custom rom with new levels! Hopefully
  this will incite folks to come up with new rom images in the future.

Also be aware that this rom image is based on v1.0 of the Arkanoid roms, so
if your PCB has the newer v2.0-based roms, there may be some differences in
gameplay.


For bootleg Arkanoid PCBs with an MCU:
--------------------------------------

I have tested these roms on bootleg Arkanoid PCBs with an MCU, and doing
the same modifications as listed above worked fine. This may not be the
case for all bootlegs.


ROM checksums:
--------------

Here are the rom checksums, for reference.

Arkanoid:
original arkatayt roms from mame:
ic81-v.3f: CRC=154e2c6f, SHA1=dce3ae1ca83b5071ebec96f3ae18b96abe828ce5
ic82-w.5f: CRC=4fa8cefa, SHA1=fb825834da9c8638e6a328784922b5dc23f16564

Arkanoid roms patched with freeplay:
ic81-v.3f: CRC=e0837f92, SHA1=1c10f9a15ff6ed2c25045edc900f4b5b71f63af8
ic82-w.5f: CRC=2442cbec, SHA1=a52c9ab90b78dbd2658072ec7939cad45a657486

Tournament Arkanoid:
original arkatour roms from mame:
a75-28.ic16: CRC=326aca4d, SHA1=5a194b7a0361236d471b24905dc6434372f81252
a75-27.ic17: CRC=e3b8faf5, SHA1=4c09478fa41881fa89ee6afb676aeb780f17ac2e

Tournament Arkanoid roms patched with freeplay:
a75-28.ic16: CRC=78f60f5f, SHA1=6fdd0d4d4a56eadb942aeb2b55f45a359cf1ca93
a75-27.ic17: CRC=d5b8444d, SHA1=52062f168bcb29ec49993804b7628e6553c3f681


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


Editing levels with ArkEdit.exe:
--------------------------------

There is a level editor for Arkanoid called ArkEdit.exe. It was designed
for older versions of MAME where the MCU was emulated or was a bootleg, so
it is looking for level offsets in the wrong place.

I have provided fake "ARKANOID.UC" MCU files that contain the proper level
offsets for both Arkanoid and Tournament Arkanoid in the respective
directories. In order to get ArkEdit.exe to recognize the roms, they
need to be renamed to "a75_01-1.rom" for the IC17 rom, and "a75_11.rom" for
the IC16 rom. Once you have the proper a75_01-1.rom, a75_11.rom, and
ARKANOID.UC files in the same directory, you should be able to open and
edit them.


- mdeslaur

Revision History:
2022-07-08 - Initial version
2022-07-21 - Version 2, added Tournament Arkanoid, and made freeplay DIP
             switch selectable.

