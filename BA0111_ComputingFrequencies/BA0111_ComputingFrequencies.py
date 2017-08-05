'''
Computing a Frequency Array

Generate the frequency array of a DNA string.

Given: A DNA string Text and an integer k.
Return: The frequency array of k-mers in Text.

Sample Dataset
ACGCGGCTCTGAAA
2
Sample Output
2 1 0 0 0 0 2 2 1 2 1 0 0 1 1 0
'''
import sys
# Stephen Blatti 08032017
infile = open('', 'r')
lines = infile.read().splitlines()
Text = lines[0]
k = int(lines[1])
infile.close()
# Text = 'ACGCGGCTCTGAAA'
# k = 2
def SymbolToNumber(symbol):
    transform = {'A':0, 'C':1, 'G':2, 'T':3}
    return transform[symbol]

def PatternToNumber(Pattern):
    if len(Pattern) == 0:
        return 0
    symbol = Pattern[-1] # last symbol(Pattern)
    Prefix = Pattern[:-1] # Prefix(Pattern)
    return 4 * PatternToNumber(Prefix) + SymbolToNumber(symbol)

def ComputingFrequencies(Text, k):
    FrequencyArray = [0] * (4 ** k)
    for i in range(0, len(Text) - k + 1):
        Pattern = Text[i:i+k]
        j = PatternToNumber(Pattern)
        FrequencyArray[j] = FrequencyArray[j] + 1
    return FrequencyArray

print(*ComputingFrequencies(Text, k))
