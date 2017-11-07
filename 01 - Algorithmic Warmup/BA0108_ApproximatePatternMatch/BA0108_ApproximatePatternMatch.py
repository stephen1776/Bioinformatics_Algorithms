'''
Approximate Pattern Matching Problem
Find all approximate occurrences of a pattern in a string.

Given: Strings Pattern and Text along with an integer d.
Return: All starting positions where Pattern appears as a substring of Text with at most d mismatches.
'''

import sys, My_BioFunctions as bf

infile = open('', 'r')
lines = infile.read().splitlines()
Pattern = lines[0]
Text = lines[1]
d = int(lines[2])
infile.close()

def ApproximatePatternMatch(Pattern, Text, d):
    count = []
    for i in range(0, len(Text) - len(Pattern) + 1):
        Pattern_p = Text[i:i + len(Pattern)]
        if bf.HammingDistance(Pattern, Pattern_p) <= d:
            count.append(i)
    return count


print(*ApproximatePatternMatch(Pattern, Text, d))