These patches add freeplay to the Double Dragon roms.
There are directories containing patches for multiple rom sets.

These need to be applied on top of the 1 and 4 rom images that match your
romset with the xdelta3.exe utility, like so:

ddragon (Double Dragon (Japan)):
xdelta3.exe -d -s old\21j-1-5.26 ddragon\21j-1-5.26.patch new\21j-1-5.26
xdelta3.exe -d -s old\21j-4-1.23 ddragon\21j-4-1.23.patch new\21j-4-1.23

ddragonw (Double Dragon (World set 1)):
xdelta3.exe -d -s old\21j-1.26 ddragonw\21j-1.26.patch new\21j-1.26
xdelta3.exe -d -s old\21j-4.23 ddragonw\21j-4.23.patch new\21j-4.23

ddragonw1 (Double Dragon (World set 2)):
xdelta3.exe -d -s old\e1-1.26 ddragonw1\e1-1.26.patch new\e1-1.26
xdelta3.exe -d -s old\e4-1.23 ddragonw1\e4-1.23.patch new\e4-1.23

ddragonu (Double Dragon (US set 1)):
xdelta3.exe -d -s old\21a-1-5.26 ddragonu\21a-1-5.26.patch new\21a-1-5.26
xdelta3.exe -d -s old\21a-4.23 ddragonu\21a-4.23.patch new\21a-4.23

ddragonua (Double Dragon (US set 2)):
xdelta3.exe -d -s old\21a-1 ddragonua\21a-1.patch new\21a-1
xdelta3.exe -d -s old\21a-4_2 ddragonua\21a-4_2.patch new\21a-4_2

ddragonub (Double Dragon (US set 3)):
xdelta3.exe -d -s old\21a-1_6.bin ddragonub\21a-1_6.bin.patch new\21a-1_6.bin
xdelta3.exe -d -s old\21a-4_2 ddragonub\21a-4_2.patch new\21a-4_2

- mdeslaur

Revision History:
2021-07-05 - Initial version

