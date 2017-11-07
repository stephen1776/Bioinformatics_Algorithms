'''
Frequent Words with Mismatches and Reverse Complements Problem
Find the most frequent k-mers (with mismatches and reverse complements) in a DNA string.

Given: A DNA string Text as well as integers k and d.
Return: All k-mers Pattern maximizing the sum Countd(Text, Pattern) + Countd(Text, Pattern) over all possible k-mers.
'''

import sys, My_BioFunctions as bf


def FrequentWordsWithMismatchesAndReverseComplement(Text, k, d):
    FrequentPatterns = 0
    Neighborhoods = []
    for i in range(0, len(Text) - k + 1):
        reverseC_DNA = bf.reverseComplement(Text[i:i + k])
        Neighborhoods = Neighborhoods + bf.Neighbors(Text[i:i + k], d) + bf.Neighbors(reverseC_DNA,d)
    count = [0] * len(Neighborhoods)
    index = [0] * len(Neighborhoods)
    for i in range(0, len(Neighborhoods)):
        Pattern = Neighborhoods[i]
        index[i] = bf.PatternToNumber(Pattern)
        count[i] = 1

    sortedIndex = sorted(index)
    for i in range(0, len(Neighborhoods) - 1):
        if sortedIndex[i] == sortedIndex[i + 1]:
            count[i + 1] = count[i] + 1
    maxCount = max(count)
    FrequentPatterns = [bf.NumberToPattern(sortedIndex[i], k) for i, u in enumerate(count) if u == maxCount]
    return FrequentPatterns

if __name__ == '__main__':
    with open('') as f:
        lines = f.read().splitlines()
    Text = lines[0]
    k = int(lines[1].split(' ')[0])
    d = int(lines[1].split(' ')[1])
    print(*FrequentWordsWithMismatchesAndReverseComplement(Text, k, d))