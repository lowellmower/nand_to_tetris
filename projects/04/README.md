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


