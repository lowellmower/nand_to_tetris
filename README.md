### [The Elements of Computing Systems](https://www.amazon.com/Elements-Computing-Systems-Building-Principles/dp/0262640686/ref=ed_oe_p)

Building a Modern Computer from First Principals

#### Goals:
- Gain understanding about where software meets hardware and expose the iceberg under the surface.
- Gain understanding about where computer science ends and physicis and electrical engineering begin.
- Become more intimately familiar with the systems of a computer which are abstracted from daily life as a developer.
- Become more fluent in terminology and topics of machine hardware and the limits / problems which said hardware faces.
- Have fun and learn something.

```bash
# CHIPSET API
  Add16(a= ,b= ,out= );
  ALU(x= ,y= ,zx= ,nx= ,zy= ,ny= ,f= ,no= ,out= ,zr= ,ng= );
  And16(a= ,b= ,out= );
  And(a= ,b= ,out= );
  ARegister(in= ,load= ,out= );
  Bit(in= ,load= ,out= );
  CPU(inM= ,instruction= ,reset= ,outM= ,writeM= ,addressM= ,pc= );
  DFF(in= ,out= );
  DMux4Way(in= ,sel= ,a= ,b= ,c= ,d= );
  DMux8Way(in= ,sel= ,a= ,b= ,c= ,d= ,e= ,f= ,g= ,h= );
  DMux(in= ,sel= ,a= ,b= );
  DRegister(in= ,load= ,out= );
  FullAdder(a= ,b= ,c= ,sum= ,carry= );
  HalfAdder(a= ,b= ,sum= , carry= );
  Inc16(in= ,out= );
  Keyboard(out= );
  Memory(in= ,load= ,address= ,out= );
  Mux16(a= ,b= ,sel= ,out= );
  Mux4Way16(a= ,b= ,c= ,d= ,sel= ,out= );
  Mux8Way16(a= ,b= ,c= ,d= ,e= ,f= ,g= ,h= ,sel= ,out= );
  Mux(a= ,b= ,sel= ,out= );
  Nand(a= ,b= ,out= );
  Not16(in= ,out= );
  Not(in= ,out= );
  Or16(a= ,b= ,out= );
  Or8Way(in= ,out= );
  Or(a= ,b= ,out= );
  PC(in= ,load= ,inc= ,reset= ,out= );
  RAM16K(in= ,load= ,address= ,out= );
  RAM4K(in= ,load= ,address= ,out= );
  RAM512(in= ,load= ,address= ,out= );
  RAM64(in= ,load= ,address= ,out= );
  RAM8(in= ,load= ,address= ,out= );
  Register(in= ,load= ,out= );
  ROM32K(address= ,out= );
  Screen(in= ,load= ,address= ,out= );
  Xor(a= ,b= ,out= );
```

### PROGRAM AND ASSEMBLER INSTRUCTIONS:

#### INSTRUCTION TABLES:

An Address Instruction (A instruction) is a 16 bit value used to set the A register's bit address space. The first of the 16 bits is the control bit and is used to signify if we should (1) or should not (0) execute something. This will play as the control pin in the multiplexers in the CPU
address:
```
EXAMPLE A INSTRUCTION:

Instruction: @value
v = is the binary rep of value - e.g. 9 == 1001

Binary for @9: 0 0 0 0 0 0 0 0 0 0 0 0 1 0 0 1
               | |___________________________|
               |        represents 9
               |
      Negative control pin
```
A Compute Instruction (C Instruction) is a 16 bit value which essentially communicate answers to three questions; 1.) What to compute, 2.) Where to store that computed value, and 3.) What to do next.
```
EXAMPLE C INSTRUCTION:

Instruction: dest=comp;jump

Note: The dest or jump fields may be empty
      If dest is empty, the "=" is omitted
      If jump is empty, the ";" is omitted

Binary: 1 1 0 0 0 0 1 1 0 0 0 0 1 0 0 1
Note: All C instructions begin with three 1

   1  1  1    0   0   0   1   1   0   0      0   0   1      0   0   1
  |1| 1  1| | a  c1  c2  c3  c4  c5  c6 | | d1  d2  d3 | | j1  j2  j3 |
  |^|__^__| |___________^_______________| |______^_____| |______^_____|
   |   |                |                        |              |
C instruction bit       |                   Destination         |
       |           Computation                  bits        Jump bits
  Unused bits          bits
```
```
COMPUTATION TABLE:
+----------------+-------------------------+---------------------+
|  (when a=0)    |    c1 c2 c3 c4 c5 c6    |     (when a=1)      |
|  comp mnemonic |                         |     comp mnemonic   |
+----------------+-------------------------+---------------------+
|      0         |     1  0  1  0  1  0    |          -          |
+----------------+-------------------------+---------------------+
|      1         |     1  1  1  1  1  1    |          -          |
+----------------+-------------------------+---------------------+
|     -1         |     1  1  1  0  1  0    |          -          |
+----------------+-------------------------+---------------------+
|      D         |     0  0  1  1  0  0    |          -          |
+----------------+-------------------------+---------------------+
|      A         |     1  1  0  0  0  0    |          M          |
+----------------+-------------------------+---------------------+
|     !D         |     0  0  1  1  0  1    |          -          |
+----------------+-------------------------+---------------------+
|     !A         |     1  1  0  0  0  1    |         !M          |
+----------------+-------------------------+---------------------+
|     -D         |     0  0  1  1  1  1    |          -          |
+----------------+-------------------------+---------------------+
|     -A         |     1  1  0  0  1  1    |         -M          |
+----------------+-------------------------+---------------------+
|     D+1        |     0  1  1  1  1  1    |          -          |
+----------------+-------------------------+---------------------+
|     A+1        |     1  1  0  1  1  1    |         M+1         |
+----------------+-------------------------+---------------------+
|     D-1        |     0  0  1  1  1  0    |          -          |
+----------------+-------------------------+---------------------+
|     A-1        |     1  1  0  0  1  0    |         M-1         |
+----------------+-------------------------+---------------------+
|     D+A        |     0  0  0  0  1  0    |         D+M         |
+----------------+-------------------------+---------------------+
|     D-A        |     0  1  0  0  1  1    |         D-M         |
+----------------+-------------------------+---------------------+
|     A-D        |     0  0  0  1  1  1    |         M-D         |
+----------------+-------------------------+---------------------+
|     D&A        |     0  0  0  0  0  0    |         D&M         |
+----------------+-------------------------+---------------------+
|     D|A        |     0  1  0  1  0  1    |         D|M         |
+----------------+-------------------------+---------------------+
```

```
DESTINATION TABLE:
+----------------+----------------+--------------------------------------------------+
|   d1 d2 d3     |    Mnemonic    |    Destination (where to store computed value)   |
+----------------+----------------+--------------------------------------------------+
|    0 0 0       |     null       |         The value is not stored anywhere         |
+----------------+----------------+--------------------------------------------------+
|    0 0 1       |      M         |    Memory[A] (memory register addressed by A)    |
+----------------+----------------+--------------------------------------------------+
|    0 1 0       |      D         |                  D register                      |
+----------------+----------------+--------------------------------------------------+
|    0 1 1       |      MD        |           Memory[A] and D register               |
+----------------+----------------+--------------------------------------------------+
|    1 0 0       |      A         |                  A register                      |
+----------------+----------------+--------------------------------------------------+
|    1 0 1       |      AM        |           A register and Memory[A]               |
+----------------+----------------+--------------------------------------------------+
|    1 1 0       |      AD        |           A register and D register              |
+----------------+----------------+--------------------------------------------------+
|    1 1 1       |      AMD       |      A register, Memory[A], and D register       |
+----------------+----------------+--------------------------------------------------+
```
EXAMPLE:
Recall that the format of the C-instruction is 111a cccc ccdd djjj. Suppose
we want the computer to increment the value of Memory[7] by 1 and to also store the
result in the D register. According to tables above, this can be accomplished by
the following instructions:
```
0000 0000 0000 0111 // @7
1111 1101 1101 1000 // MD=M+1
```
```
JUMP TABLE:
+----------------------------------+----------------+-------------------+
|     j1          j2        j3     |    Mnemonic    |       Effect      |
|  (out < 0)  (out = 0)  (out > 0) |                |                   |
+----------------------------------+----------------+-------------------+
|     0           0          0     |      null      |      No jump      |
+----------------------------------+----------------+-------------------+
|     0           0          1     |      JGT       |  If out > 0 jump  |
+----------------------------------+----------------+-------------------+
|     0           1          0     |      JEQ       |  If out ¼ 0 jump  |
+----------------------------------+----------------+-------------------+
|     0           1          1     |      JGE       |  If out b 0 jump  |
+----------------------------------+----------------+-------------------+
|     1           0          0     |      JLT       |  If out < 0 jump  |
+----------------------------------+----------------+-------------------+
|     1           0          1     |      JNE       |  If out 0 0 jump  |
+----------------------------------+----------------+-------------------+
|     1           1          0     |      JLE       |  If out a 0 jump  |
+----------------------------------+----------------+-------------------+
|     1           1          1     |      JMP       |       Jump        |
+----------------------------------+----------------+-------------------+
```
