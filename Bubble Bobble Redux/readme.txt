These patches add freeplay to the Bubble Bobble Redux roms.

They were ported from patches that appeared for the original Bubble Bobble
roms and were available in this forum thread:

http://www.jammaplus.co.uk/forum/forum_posts.asp?TID=70581

Unfortunately, jammaplus.co.uk went away, so I don't know who the author of
the original patches is. If you know who it is, please let me know.

There are two different versions of the Redux roms: the base romset which
is the version included in mame as the "bbredux" set, and a second romset
which includes the extra patches from Redux that added level skipping,
game continues, and high score saves.

If you are using the base romset, apply the following patches:

xdelta3.exe -d -s old\bb3 bb3_freeplay.patch new\bb3
xdelta3.exe -d -s old\bb4 bb4_freeplay.patch new\bb4

If you are using the full incremental set of Redux patches, including level
skipping, game continues, and high score saves, apply the following
patches:

xdelta3.exe -d -s old\bb3 bb3_inc_freeplay.patch new\bb3
xdelta3.exe -d -s old\bb4 bb4_inc_freeplay.patch new\bb4

- mdeslaur

Revision History:
2021-07-09 - Version 2: change Insert Coin text, add patches for both
             base redux roms and the incremental patched ones.
2018-12-07 - Initial version.

