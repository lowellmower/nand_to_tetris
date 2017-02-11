###2A instrud1io3j 2A instrud1io3:
Can be symbolically represented as `@{VAL}` where VAL is equal to any integer <=32767(=2^15 -1)

### C instruciton:
Can be symbolically represented as `dest = comp ; jump` e.g. `M=-1;JQE` represented as 16 bits it looks like:
```bash
   1  1  1  a  c1  c2  c3  c4  c5  c6  d1  d2  d3  j1  j2  j3
  | ||n\a |        COMP                 DEST          JUMP

COMP = binary to map to computation table
DEST = binary to map to 8 different desitinations on a destination table
JUMP = binary to map to 8 different jump conditions on jump table
```

### Screen
I/O Screen Output Memory Map - 256 x 512 (0..255 x 0..511) X / Y coord plane. At each intreceies lay a pixel. For every pixel there is a bit, 1 = on / 0 = off

Integer division to access a pixel:

i = 32*row + col/16

1:
word = SCREEN[32*row + col/16]
word = RAM[16384 + 32*row + col/16]
2:
set the (col % 16)th bit to 0/1
3:
Commit the word to RAM

### Keyboard
I/O Keyboard Memory Map - transfers scan codes to binary and maps to a memory map e.g. k = 75 which then represents the binary code. An idle keyboard is 0
KBD
