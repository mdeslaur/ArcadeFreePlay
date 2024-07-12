These patches add freeplay to the Bank Panic roms.

These need to be applied on top of the 7H and 7E rom images with the
xdelta3.exe utility, like so:

xdelta3.exe -d -s old\epr-6173.7h epr-6173.7h.patch new\epr-6173.7h
xdelta3.exe -d -s old\epr-6175.7e epr-6175.7e.patch new\epr-6175.7e

- mdeslaur

Revision History:
2021-06-28 - Initial version

