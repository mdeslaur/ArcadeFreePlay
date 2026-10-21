#!/usr/bin/env python3
# Encrypt/decrypt Braze mario_13.bin rom
#
# Marc Deslauriers <marcdeslauriers@videotron.ca>
#

import sys

# MAME convention: bitswap<8>(val, b7..b0) -> output bit i = input bit b<i>.
# Internally src[i] = source bit for output bit i.
def _src_from_mame(mame):
    # mame = (b7, b6, ..., b0): output bit 7 takes input bit b7, etc.
    src = [0] * 8
    for i in range(8):
        src[i] = mame[7 - i]
    return src
ADDR_PERM = _src_from_mame((7, 2, 3, 1, 0, 6, 4, 5))
BYTE_PERM = _src_from_mame((1, 4, 5, 7, 6, 0, 3, 2))

def bitswap(byte, src):
    out = 0
    for i in range(8):
        out |= ((byte >> src[i]) & 1) << i
    return out

def inverse(src):
    inv = [0] * 8
    for i in range(8):
        inv[src[i]] = i
    return inv

def process(data, encrypt):
    aperm, bperm = (ADDR_PERM, BYTE_PERM) if not encrypt else (inverse(ADDR_PERM), inverse(BYTE_PERM))
    dest = bytearray(len(data))
    for mem in range(len(data)):
        newmem = (bitswap(mem >> 8, aperm) << 8) | (mem & 0xFF)
        dest[newmem] = bitswap(data[mem], bperm)
    return dest

def main():
    if len(sys.argv) != 4 or sys.argv[1] not in ("enc", "dec"):
        print(f"usage: {sys.argv[0]} <enc|dec> <in.bin> <out.bin>", file=sys.stderr)
        sys.exit(1)
    encrypt = sys.argv[1] == "enc"
    with open(sys.argv[2], "rb") as f:
        data = f.read()
    if len(data) > 0x10000:
        print("error: file larger than 0x10000 bytes", file=sys.stderr)
        sys.exit(1)
    with open(sys.argv[3], "wb") as f:
        f.write(process(data, encrypt))

if __name__ == "__main__":
    main()
