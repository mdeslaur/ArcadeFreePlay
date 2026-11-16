#!/usr/bin/python3
#
# decrypt mspactwin rom with a list of opcode addresses
# Marc Deslauriers
#
# 2026-11-16: initial release
#

import binascii
import sys

def read_rom(romfile):
    '''read in a romfile'''
    f = open(romfile, "rb")
    contents = f.read()
    f.close()
    return contents

def read_opcodes(opcodes):
    '''read in a file containing a list of opcode offsets'''
    contents = []
    f = open(opcodes, "rb")
    for line in f.readlines():
        splitline = line.split()
        try:
            address = int(splitline[0][:4], 16)
            # Rom is split into two memory locations
            if address >= 0x8000:
                address -= 0x4000
        except:
            pass
        contents.append(address)
    f.close()
    return contents

def write_rom(romfile, contents):
    '''write out romfile'''
    f = open(romfile, "wb")
    f.write(contents)
    f.close()

def calc_sum16(contents):
    '''calculate sum16'''
    checksum = 0
    for byte in contents:
        checksum += byte
    checksum &= 0xFFFF
    #print("ROM Checksum is %s" % hex(checksum))
    return checksum

def adjust_sum16(contents, old, new):
    '''adjust sum16'''

    # At offset 0x1747, there's a few hundred unused 0xFF bytes we can
    # modify to get a matching sum16
    offset = 0x1747
    need = abs(new + 0x10000 - old)
    num_bytes, last_byte = divmod(need,0xFF)

    for num in range(num_bytes):
        contents[num + offset] = 0x00;
    contents[num_bytes + offset] = 0xFF - last_byte;

    return contents

def bitswap(data, order, xor=None):
    '''Swaps bits in a byte, optionally does xor first'''

    if xor is not None:
        #print("MD using xor %s on data %s" % (hex(xor), hex(data)))
        data = data ^ xor
        #print("MD new data is %s" % (hex(data)))

    # Mame specifies MSB first
    # Reverse it so we can use enumerate()
    order.reverse()

    newbyte = 0
    for new_pos, old_pos in enumerate(order):
        bit = (data >> old_pos) & 1
        newbyte |= (bit << new_pos)
    return newbyte

def decrypt_rom(rom, opcodes):
    '''Decrypt the rom using the list of opcode offsets'''

    new_rom = bytearray(len(rom))
    # Stolen from MAME's pacman.cpp:
    #
    #for (int A = 0x0000; A < 0x4000; A+=2)
    #{
    #    // decode opcode
    #    m_decrypted_opcodes     [A  ] = bitswap<8>(rom[       A  ]       , 4, 5, 6, 7, 0, 1, 2, 3);
    #    m_decrypted_opcodes     [A+1] = bitswap<8>(rom[       A+1] ^ 0x9A, 6, 4, 5, 7, 2, 0, 3, 1);
    #    m_decrypted_opcodes_high[A  ] = bitswap<8>(rom[0x8000+A  ]       , 4, 5, 6, 7, 0, 1, 2, 3);
    #    m_decrypted_opcodes_high[A+1] = bitswap<8>(rom[0x8000+A+1] ^ 0x9A, 6, 4, 5, 7, 2, 0, 3, 1);
    #
    #    // decode operand
    #    rom[       A  ] = bitswap<8>(rom[       A  ]       , 0, 1, 2, 3, 4, 5, 6, 7);
    #    rom[       A+1] = bitswap<8>(rom[       A+1] ^ 0xA3, 2, 4, 6, 3, 7, 0, 5, 1);
    #    rom[0x8000+A  ] = bitswap<8>(rom[0x8000+A  ]       , 0, 1, 2, 3, 4, 5, 6, 7);
    #    rom[0x8000+A+1] = bitswap<8>(rom[0x8000+A+1] ^ 0xA3, 2, 4, 6, 3, 7, 0, 5, 1);
    #}

    for offset in range(len(rom)):
        if offset in opcodes:
            #print("MD offset %s is in opcode list" % offset)
            if offset % 2 == 0:
                xor = None
                bit_order = [4, 5, 6, 7, 0, 1, 2, 3]
            else:
                xor = 0x9A
                bit_order = [6, 4, 5, 7, 2, 0, 3, 1]
        else:
            #print("MD offset %s is not in opcode list" % offset)
            if offset % 2 == 0:
                xor = None
                bit_order = [0, 1, 2, 3, 4, 5, 6, 7]
            else:
                xor = 0xA3
                bit_order = [2, 4, 6, 3, 7, 0, 5, 1]

        new_rom[offset] = bitswap(rom[offset], bit_order, xor)
        #print("MD new byte is %s" % hex(new_rom[offset]))

    return new_rom


if len(sys.argv) in [2, 3]:
    rom_filename = "m27256.bin"
    print("Reading: %s" % rom_filename)
    rom = read_rom(rom_filename)
    rom = bytearray(rom)
    #orisum = calc_sum16(rom)

    if len(sys.argv) == 2:
        opcode_file = sys.argv[1]
    elif len(sys.argv) == 3:
        opcode_file = sys.argv[2]
    print("Reading: %s" % opcode_file)
    opcodes = read_opcodes(opcode_file)
    #print("opcodes = %s" % opcodes)

    print("Decrypting rom...")
    newrom = decrypt_rom(rom, opcodes)
    #newsum = calc_sum16(rom)

    if len(sys.argv) == 2 or sys.argv[1] == "default":
        newfile = "m27256dec.bin"
        print("Writing: %s" % newfile)
        write_rom(newfile, newrom)
    elif sys.argv[1] == "pacman":
        print("Writing boot1")
        write_rom("boot1", newrom[0x0000:0x1000])
        print("Writing boot2")
        write_rom("boot2", newrom[0x1000:0x2000])
        print("Writing boot3")
        write_rom("boot3", newrom[0x2000:0x3000])
        print("Writing boot4")
        write_rom("boot4", newrom[0x3000:0x4000])
        print("Writing boot5")
        write_rom("boot5", newrom[0x4000:0x5000])
        print("Writing boot6")
        write_rom("boot6", newrom[0x5000:0x6000])
    elif sys.argv[1] == "512":
        full_rom = newrom[0x0000:0x4000]
        full_rom += bytearray([0] * 0x4000)
        full_rom += newrom[0x4000:0x8000]
        full_rom += bytearray([0] * 0x4000)
        print("Writing 27512.bin")
        write_rom("27512.bin", full_rom)
else:
    print("Incorrect parameters!")
    print("Usage: ./mspactwin-decrypt.py <type> <opcodelist>")
    print("Where <type> is default: decrypt rom and create m27256dec.bin")
    print("                 pacman: decrypt rom and create pacman images (boot1-boot6)")
    print("                    512: decrypt rom and create 27512.bin with no gaps")
