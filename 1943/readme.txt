These patches add freeplay to the 1943 roms.
There are directories containing patches for multiple rom sets.

Listed below are the checksums for the various 12b roms to determine which
rom set is present on a particular board.

These need to be applied on top of the rom image for 12d that matches your
romset with the xdelta3.exe utility, like so:

xdelta3.exe -d -s OLDROMFILENAME PATCHFILENAME NEWROMFILENAME

1943u (1943: The Battle of Midway (US, Rev C)):
CRC(c686cc5c) SHA1(5efb2d9df737564d599f71b71a6438f7624b27c3)
xdelta3.exe -d -s old\bmu01c.12d 1943u\bmu01c.12d.patch new\bmu01c.12d

1943ua (1943: The Battle of Midway (US)):
CRC(793cf15f) SHA1(7d49fd17acad7900c3d1187d25ada14247e267f3)
xdelta3.exe -d -s old\bmu01.12d 1943ua\bmu01.12d.patch new\bmu01.12d

1943j (1943: Midway Kaisen (Japan, Rev B)):
CRC(363f9f3d) SHA1(06fbdf1fa2304a000bcb0a151b2ef4be8b291b0b)
xdelta3.exe -d -s old\bm01b.12d 1943j\bm01b.12d.patch new\bm01b.12d

1943ja (1943: Midway Kaisen (Japan)):
CRC(232df705) SHA1(04d97853d5edef8a6126c81febadbdeda373df29)
xdelta3.exe -d -s old\bm01.12d 1943ja\bm01.12d.patch new\bm01.12d

1943b (1943: Battle of Midway (bootleg, hack of Japan set)):
CRC(9a2d70ab) SHA1(6f84e906656f132ffcb63022f6d067580d261431)
xdelta3.exe -d -s old\1.12d 1943b\1.12d.patch new\1.12d

1943bj (1943: Midway Kaisen (bootleg)):
CRC(b3b7c7cd) SHA1(6197023f4384fd2ac72b686c26a6ff2877345b61)
xdelta3.exe -d -s old\mkb03.12d 1943bj\mkb03.12d.patch new\mkb03.12d

- mdeslaur

Revision History:
2024-07-12 - Initial version

