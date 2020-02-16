# Linear_approximation_table_script
This is my University work from cryptography course. This is a script, which takes an subtitution, and creates a linear approximation table for it.
In cryptography, linear cryptanalysis is a general form of cryptanalysis based on finding affine approximations to the action of a cipher. Attacks have been developed for block ciphers and stream ciphers. Linear cryptanalysis is one of the two most widely used attacks on block ciphers; the other being differential cryptanalysis.

## Example:
For following substitution (5,8,1,13,10,3,4,2,14,15,12,7,6,0,9,11)
Script created following exel table, which can be used for linear cryptoanalysis:

| 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 | 11 | 12 | 13 | 14 | 15 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
0|8|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0
1|0|-2|-2|0|2|0|4|-2|2|0|0|2|4|2|-2|0
2|0|-2|0|-2|4|2|0|-2|-2|0|-2|0|-2|0|2|-4
3|0|0|2|-2|-2|-2|0|-4|4|0|-2|-2|-2|2|0|0
4|0|-4|2|-2|0|-4|-2|2|0|0|2|2|0|0|-2|-2
5|0|2|0|-2|2|-4|2|0|-2|-4|-2|0|0|-2|0|2
6|0|-2|2|0|0|-2|2|0|-2|4|0|-2|2|0|4|2
7|0|0|4|0|2|2|2|-2|0|0|4|0|-2|-2|-2|2
8|0|4|2|-2|0|0|2|2|0|4|-2|2|0|0|-2|-2
9|0|2|0|-2|2|0|-2|0|-2|0|2|0|0|    6|0|2
10|0|-2|2|0|0|2|-2|0|-2|0|-4|-2|2|0|-4|2
11|0|0|-4|0|2|-2|-2|-2|0|4|0|0|-2|-2|-2|2
12|0|0|0|0|-4|0|0|-4|-4|0|0|4|0|0|0|0
13|0|-2|-2|0|-2|0|4|2|-2|0|0|-2|-4|2|-2|0
14|0|-2|0|-2|0|2|0|2|2|0|-2|4|-2|0|2|4
15|0|0|2|    6|2|-2|0|0|0|0|-2|2|-2|2|0|0
