#Stephen Blatti
import sys
def SymbolToNumber(symbol):
    d = {'A':0, 'C':1, 'G':2, 'T':3}
    return d[symbol]

def NumberToSymbol(number):
    d = {0:'A', 1:'C', 2:'G', 3:'T'}
    return d[number]

def PatternToNumber(Pattern):
    if len(Pattern) == 0:
        return 0
    symbol = Pattern[-1] # last symbol(Pattern)
    Prefix = Pattern[:-1] # Prefix(Pattern)
    return 4 * PatternToNumber(Prefix) + SymbolToNumber(symbol)

def NumberToPattern(index, k):
    if k ==1:
        return NumberToSymbol(index)
    prefixIndex = int(index / 4)
    r = index % 4 # remainder(index,4)
    symbol = NumberToSymbol(r)
    PrefixPattern = NumberToPattern(prefixIndex, k - 1)
    return PrefixPattern + symbol

def ComputingFrequencies(Text, k):
    FrequencyArray = [0] * (4 ** k)
    for i in range(0, len(Text) - k + 1):
        Pattern = Text[i:i+k]
        j = PatternToNumber(Pattern)
        FrequencyArray[j] = FrequencyArray[j] + 1
    return FrequencyArray

def HammingDistance(DNA1, DNA2):
    hamDist = [0]
    if len(DNA1) != len(DNA2):
        raise ValueError("Undefined for sequences of unequal length")
    for i in range(0, len(DNA1)):
        hamDist = sum(u != v for u,v in zip(DNA1, DNA2))
    return hamDist
