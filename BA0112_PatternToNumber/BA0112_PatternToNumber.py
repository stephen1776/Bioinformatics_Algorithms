'''
Implement PatternToNumber
Convert a DNA string to a number.

Given: A DNA string Pattern.
Return: PatternToNumber(Pattern).

Sample Dataset
AGT
Sample Output
11

'''
import sys
# Stephen Blatti 08022017
infile = open('', 'r')
lines = infile.read().splitlines()
Pattern = lines[0]
# na = lines[1]

#Pattern = 'AGT'
def SymbolToNumber(symbol):
    transform = {'A':0, 'C':1, 'G':2, 'T':3}
    return transform[symbol]
def PatternToNumber(Pattern):
    if len(Pattern) == 0:
        return 0
    symbol = Pattern[-1] # last symbol(Pattern)
    Prefix = Pattern[:-1] # Prefix(Pattern)
    return 4 * PatternToNumber(Prefix) + SymbolToNumber(symbol)
outFile = open("PatternToNumber_output.txt", "w")
outFile.write('{}'.format(PatternToNumber(Pattern)))
outFile.close()