'''

Implement NumberToPattern

Convert an integer to its corresponding DNA string.

Given: Integers index and k.
Return: NumberToPattern(index, k).

Sample Dataset
45
4

Sample Output
AGTC

'''

# Stephen Blatti 08032017
import sys, My_BioFunctions as Bfctn


infile = open('', 'r')
lines = infile.read().splitlines()
index = int(lines[0])
k = int(lines[1])
infile.close()

def NumberToPattern(index, k):
    if k ==1:
        return Bfctn.NumberToSymbol(index)
    prefixIndex = int(index / 4)
    r = index % 4 # remainder(index,4)
    symbol = Bfctn.NumberToSymbol(r)
    PrefixPattern = NumberToPattern(prefixIndex, k - 1)
    return PrefixPattern + symbol
print(NumberToPattern(index, k))