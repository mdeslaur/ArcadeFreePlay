These patches add freeplay to the Arkanoid: Revenge of Doh roms.
There are directories containing patches for the multiple country
specific rom sets.

These need to be applied on top of the 11C and 3E rom images with the
xdelta3.exe utility.


arknoid2 - Arkanoid - Revenge of DOH (World)
--------------------------------------------
xdelta3.exe -d -s b08__05.11c b08__05.11c.patch b08__05.11c.patched
xdelta3.exe -d -s eb08__13.3e b08__13.3e.patch b08__13.3e.patched


arknoid2u - Arkanoid - Revenge of DOH (US)
------------------------------------------
xdelta3.exe -d -s b08__11.11c b08__11.11c.patch b08__11.11c.patched
xdelta3.exe -d -s b08__12.3e b08__12.3e.patch b08__12.3e.patched


arknoid2j - Arkanoid - Revenge of DOH (Japan)
---------------------------------------------
xdelta3.exe -d -s b08_05.11c b08_05.11c.patch b08_05.11c.patched
xdelta3.exe -d -s b08_06.3e b08_06.3e.patch b08_06.3e.patched


arknoid2b - Arkanoid - Revenge of DOH (Japan bootleg)
-----------------------------------------------------
xdelta3.exe -d -s boot.11c boot.11c.patch boot.11c.patched
xdelta3.exe -d -s b08_13.3e b08_13.3e.patch b08_13.3e.patched


What about saving high scores?
------------------------------
Good news! Matt Osborn has a patch that allows saving high scores if one
of the ram chips is replaced with non-volatile memory, more information
can be found on his website here:

https://scoresaves.com/DohHS.html

As a convenience, in each directory there is a patch file that ends with
.hss which includes both my freeplay mod and Matt's high score save mod,
and can be used instead of the patch files listed above.

It is not recommended to use the high score save patch if the ram has not
been replaced, or it will break the high score display at the top of the
screen.

Have fun, and best of luck fighting XORG!

- mdeslaur

Revision History:
2025-02-15 - Initial version

