These patches add freeplay to the Bomb Jack roms.
These apply to the "Bomb Jack (set 1)" set found in mame.

These need to be applied on top of the 9, 11, 12 and 13 rom images with the
xdelta3.exe utility, like so:

xdelta3.exe -d -s old\09_j01b.bin 09_j01b.bin.patch new\09_j01b.bin
xdelta3.exe -d -s old\11_m01b.bin 11_m01b.bin.patch new\11_m01b.bin
xdelta3.exe -d -s old\12_n01b.bin 12_n01b.bin.patch new\12_n01b.bin
xdelta3.exe -d -s old\13.1r 13.1r.patch new\13.1r

- mdeslaur

Revision History:
2021-06-30 - Initial version

