These patches add freeplay to the Atari Starship 1 roms.

Unfortunately, there is no easy way to replace the original Signetics 2600
masked roms with an Eprom as the pinouts are different, an adapter has to
be made to do so. See more info in this thread about Sprint 2:
https://forums.arcade-museum.com/threads/kee-atari-sprint-2-damaged-rom-help.403980/

Once you have made adapters for two of the roms, make sure they work
properly by testing with the original rom images from MAME. After the
adapters have been tested, you can apply the freeplay patches like so:

xdelta3.exe -d -s old\7530-02.h3 7530-02.h3.patch new\7530-02.h3
xdelta3.exe -d -s old\7531-02.e3 7531-02.e3.patch new\7531-02.e3

Freeplay is enabled by setting DIP switches A, B, and C to ON.

- mdeslaur

Revision History:
2023-06-14 - Initial version.

