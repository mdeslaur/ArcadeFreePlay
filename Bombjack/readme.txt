Note: Arcade Rom Patcher v15 now has a better Free Play and High Score Save
patch, use that instead of this one.

---------------------------------------------------------------------------

These patches add freeplay to the Bomb Jack roms.
These apply to the "Bomb Jack (set 1)" set found in mame.

These need to be applied on top of the 9, 11, 12 and 13 rom images with the
xdelta3.exe utility, like so:

xdelta3.exe -d -s old\09_j01b.bin 09_j01b.bin.patch new\09_j01b.bin
xdelta3.exe -d -s old\11_m01b.bin 11_m01b.bin.patch new\11_m01b.bin
xdelta3.exe -d -s old\12_n01b.bin 12_n01b.bin.patch new\12_n01b.bin
xdelta3.exe -d -s old\13.1r 13.1r.patch new\13.1r

What about saving high scores?
------------------------------
Good news! Jrok has a patch that allows saving high scores if one of the
ram chips is replaced with non-volatile memory, more information can be
found on his website here:

https://www.jrok.com/sohs/bjack_shs.html

As a convenience, there is a patch file called 09_j01b.bin.fpshs.patch
which includes both my freeplay mod and Jrok's save high score mod, and can
be used instead of the patch file for one of the roms listed above.

xdelta3.exe -d -s old\09_j01b.bin 09_j01b.bin.fpshs.patch new\09_j01b.bin
(do the other 3 roms as above)

It is not recommended to use the high score save patch if the ram has not
been replaced, as the game will always start with the high score table set
to 0.

- mdeslaur

Revision History:
2021-06-30 - Initial version
2025-12-23 - Added high score saving rom patch
2025-12-24 - Added note about Arcade Rom Patcher

