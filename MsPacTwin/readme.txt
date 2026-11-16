The python script in this directory will decrypt the Ms Pac Man Twin
(mspactwin) romset in MAME so it can run on real Pac-Man hardware.

It can generate three types of outputs:

- A decrypted rom to work in MAME (with the MAME patch in the extras
  directory)
- A romset that works with Pac-Man boards that have been modified to run
  the 6-rom bootleg MsPacMan roms.
  (see: https://www.pinrepair.com/video/pacman.htm#hack3 and the
  "mspacmab" romset in MAME)
- A full-address 27512 rom image that can be used with a small pcb adapter
  in the CPU socket (TBA soon)


Usage: ./mspactwin-decrypt.py (type) (opcodelist)  
Where (type) is default: decrypt rom and create m27256dec.bin  
                pacman: decrypt rom and create pacman images (boot1-boot6)  
                512: decrypt rom and create 27512.bin with no gaps  

- mdeslaur

Revision History:
2026-11-16 - Initial version

