#!/usr/bin/env python3
# Recalculate the Mario Bros (Braze high-score kit) ROM checksum and fix padding.
#
# Marc Deslauriers <marcdeslauriers@videotron.ca>
#
#
# The boot-time self-test at CPU 0xe13f sums the entire 32KB ROM as 16-bit
# little-endian words (two passes: file 0x0000-0x5fff, then file 0x6000-0x7fff
# mapped at CPU 0xe000) and requires the total to be exactly 0x0000. If it is
# not, the game prints "ROM FAILURE" at the bottom of the screen and halts.
#
# This tool computes the current word sum and rewrites the compensating word in
# the unused 0xff filler region at file offset 0x6340 (CPU 0xe340) so the total
# returns to zero. It works on decrypted ROM images; use mario13_crypt.py to
# encrypt the result for MAME.
#
# usage: fix_checksum.py <decrypted.bin> [out.bin]
#        (without out.bin the file is updated in place)


import sys

ROM_SIZE = 0x8000          # 32KB ROM file
PAD_OFFSET = 0x6340        # compensating word location (0xff filler area)
PAD_END = 0x7000           # end of the filler region (sanity bound)


def word_sum(rom):
    """16-bit little-endian word sum of the whole ROM, as the game computes it."""
    return sum(rom[i] | (rom[i + 1] << 8) for i in range(0, len(rom), 2)) & 0xFFFF


def fix(rom):
    if len(rom) != ROM_SIZE:
        raise SystemExit(f"error: expected {ROM_SIZE} bytes, got {len(rom)}")
    if not (PAD_OFFSET + 2 <= PAD_END):
        raise SystemExit("error: padding word does not fit in filler region")

    old = rom[PAD_OFFSET] | (rom[PAD_OFFSET + 1] << 8)
    cur = word_sum(rom)
    comp = (old - cur) & 0xFFFF   # word that makes the total zero

    rom[PAD_OFFSET] = comp & 0xFF
    rom[PAD_OFFSET + 1] = comp >> 8

    new = word_sum(rom)
    if new != 0:
        raise SystemExit(f"error: checksum fix failed (sum is {new:#06x})")
    return cur, comp


def main():
    if len(sys.argv) not in (2, 3):
        print(f"usage: {sys.argv[0]} <decrypted.bin> [out.bin]", file=sys.stderr)
        sys.exit(1)

    src = sys.argv[1]
    dst = sys.argv[2] if len(sys.argv) == 3 else src

    with open(src, "rb") as f:
        rom = bytearray(f.read())

    cur, comp = fix(rom)

    with open(dst, "wb") as f:
        f.write(rom)

    print(f"old word sum: {cur:#06x}")
    print(f"compensation word at {PAD_OFFSET:#06x}: {comp:#06x} "
          f"({comp & 0xFF:#04x} {comp >> 8:#04x})")
    print(f"new word sum: {word_sum(rom):#06x}")
    print(f"wrote {dst}")


if __name__ == "__main__":
    main()
