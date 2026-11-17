#!/usr/bin/python3
#
# Decrypt Naughty Mouse (set 1) (nmouse) rom file
# Marc Deslauriers <marcdeslauriers@videotron.ca>
#

def swap_program(in_byte):
    '''Swaps D3 and D5 of a byte'''
    #print("type is %s" % type(in_byte))
    binary = '{:08b}'.format(in_byte)
    #print("In byte is %s" % binary)

    # Swap bits D3 and D5
    # 7,6,3,4,5,2,1,0
    # 0,1,4,3,2,5,6,7
    new_binary = binary[0:2] + binary[4] + binary[3] + binary[2] + binary[5:]
    #print("New byte is %s" % new_binary)
    #print("New int is %s" % int(new_binary, 2))
    return int(new_binary, 2)

def swap_graphics(in_byte):
    '''Swaps D4 and D6 of a byte'''
    binary = '{:08b}'.format(in_byte)
    #print("In byte is %s" % binary)
    # Swap bits D4 and D6
    # 7,4,5,6,3,2,1,0
    # 0,3,2,1,4,5,6,7
    new_binary = binary[0] + binary[3] + binary[2] + binary[1] + binary[4:]
    #print("New byte is %s" % new_binary)
    #print("New int is %s" % hex(int(new_binary, 2)))
    return int(new_binary, 2)

def swap_address(in_add):
    '''Swaps A0 and A2 of an address'''

    binary = '{:016b}'.format(in_add)
    #print("In address is %s" % binary)

    # Swap bits A0 and A2
    # 15..7,6,5,4,3,0,1,2
    # 0..8,9,10,11,12,15,14,13
    new_binary = binary[0:13] + binary[15] + binary[14] + binary[13]
    #print("New address is %s" % new_binary)
    return int(new_binary, 2)

def convert_program_rom(orig_rom):
    '''unmangles a program rom'''

    new_rom = []
    for byte in orig_rom:
        new_rom.append(swap_program(byte))

    return new_rom

def convert_graphics_rom(orig_rom):
    '''unmangles a graphics rom'''

    new_rom = []
    for i in range(len(orig_rom)):
        #print("Address: %s" % hex(i))
        new_add = swap_address(i)
        #print("New address: %s" % hex(new_add))
        new_byte=swap_graphics(orig_rom[new_add])
        new_rom.append(new_byte)

    return new_rom

def read_rom(romfile):
    '''read in a romfile'''
    f = open(romfile, "rb")
    contents = f.read()
    f.close()
    return contents

def write_rom(romfile, contents):
    '''write a romfile'''
    f = open(romfile, "wb")
    for byte in contents:
        f.write(byte.to_bytes(1, byteorder="little"))
    f.close()

def replace_int(orig_rom):
    '''replace interrupts'''
    ints = { 0xbf : 0x3c, 0xc6 : 0x40 }
    for i in range(len(orig_rom)):
        if orig_rom[i] == 0x3e and \
           orig_rom[i+2] == 0xd3 and \
           orig_rom[i+3] == 0x00:
            orig_rom[i+1] = ints.get(orig_rom[i+1], orig_rom[i+1])
    return orig_rom

# Convert main CPU roms
contents = read_rom("naumouse.d7")
contents += read_rom("naumouse.d6")
new_contents = convert_program_rom(contents)
write_rom("pacman.6e", new_contents)

contents = read_rom("naumouse.e7")
contents += read_rom("naumouse.e6")
new_contents = convert_program_rom(contents)
write_rom("pacman.6f", new_contents)

contents = read_rom("naumouse.h7")
contents += read_rom("naumouse.h6")
new_contents = convert_program_rom(contents)
# Replace Interrupt vectors with pac-man ones
new_contents = replace_int(new_contents)
write_rom("pacman.6h", new_contents)

contents = read_rom("naumouse.j7")
contents += read_rom("naumouse.j6")
new_contents = convert_program_rom(contents)
# Replace Interrupt vectors with pac-man ones
new_contents = replace_int(new_contents)
write_rom("pacman.6j", new_contents)

# Convert graphics roms
contents = read_rom("naumouse.d5")
contents += read_rom("naumouse.h5")
new_contents = convert_graphics_rom(contents)
write_rom("pacman.5e", new_contents)

contents = read_rom("naumouse.e5")
contents += read_rom("naumouse.j5")
new_contents = convert_graphics_rom(contents)
write_rom("pacman.5f", new_contents)

