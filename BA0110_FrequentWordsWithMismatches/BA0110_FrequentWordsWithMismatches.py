'''
Find the most frequent k-mers with mismatches in a string.

Given: A string Text as well as integers k and d.
Return: All most frequent k-mers with up to d mismatches in Text.
'''

import sys, My_BioFunctions as bf

def FrequentWordsWithMisMatches(Text, k, d):
    FrequentPatterns = []
    Close = [0] * 4**k
    FrequencyArray = [0] * 4**k
    for i in range(0, len(Text) - k + 1):
        Neighborhood = bf.Neighbors(Text[i: i + k], d)
        for Pattern in Neighborhood:
            index = bf.PatternToNumber(Pattern)
            Close[index] = 1
    for i in range(0, 4**k):
        if Close[i] == 1:
            Pattern = bf.NumberToPattern(i,k)
            FrequencyArray[i] = bf.ApproximatePatternCount(Text, Pattern, d)
    maxCount = max(FrequencyArray)
    for i in range(0, 4**k):
        if FrequencyArray[i] == maxCount:
            Pattern = bf.NumberToPattern(i,k)
            FrequentPatterns.append(Pattern)
    return FrequentPatterns


def FrequentWordsWithMismatchesBySorting(Text, k, d):
    FrequentPatterns = 0
    Neighborhoods = []
    for i in range(0, len(Text) - k + 1):
        Neighborhoods = Neighborhoods + bf.Neighbors(Text[i:i + k], d)

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
    with open('data/rosalind_ba1i.txt') as f:
        lines = f.read().splitlines()
    Text = lines[0]
    k = int(lines[1].split(' ')[0])
    d = int(lines[1].split(' ')[1])
    print(*FrequentWordsWithMismatchesBySorting(Text, k, d))
