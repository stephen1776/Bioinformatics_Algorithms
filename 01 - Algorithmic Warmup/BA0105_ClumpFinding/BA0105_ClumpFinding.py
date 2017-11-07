'''
Given integers L and t, a string Pattern forms an (L, t)-clump inside a (larger) string Genome if
there is an interval of Genome of length L in which Pattern appears at least t times.
For example, TGCA forms a (25,3)-clump in the following
Genome: gatcagcataagggtcccTGCAATGCATGACAAGCCTGCAgttgttttac.

Implement Clump Finding
Find patterns forming clumps in a string.

Given: A string Genome, and integers k, L, and t.
Return: All distinct k-mers forming (L, t)-clumps in Genome.

Sample Dataset
CGGACTCGACAGATGTGAAGAAATGTGAAGACTGAGTGAAGAGAAGAGGAAACACGACACGACATTGCGACATAATGTACGAATGTAATGTGCCTATGGC
5 75 4

Sample Output
CGACA GAAGA AATGT

'''
# Stephen Blatti 08022017
import sys, My_BioFunctions as my_bf

infile = open('', 'r')
lines = infile.read().splitlines()
Genome = lines[0]
klt = lines[1].split()
k = int(klt[0])
L = int(klt[1])
t = int(klt[2])
infile.close()

def ClumpFinding(Genome, k, t, L):
    FrequentPatterns = []
    Clump = [0] * 4**k
    for i in range(0, len(Genome) - L + 1):
        Text = Genome[i:i+L]
        FrequencyArray = my_bf.ComputingFrequencies(Text, k)
        for index in range(0, 4**k):
            if FrequencyArray[index] >= t:
                Clump[index] = 1
    for i in range(0, 4**k):
        if Clump[i] == 1:
            Pattern = my_bf.NumberToPattern(i, k)
            FrequentPatterns.append(Pattern)
    return FrequentPatterns

# print(*ClumpFinding(Genome, k, t, L))

def BetterClumpFinding(Genome, k, t, L):
    FrequentPatterns = []
    Clump = [0] * 4 ** k
    Text = Genome[0:L]
    FrequencyArray = my_bf.ComputingFrequencies(Text, k)
    for i in range(0, 4**k):
        if FrequencyArray[i] >= t:
            Clump[i] = 1
    for i in range(1, len(Genome) - L + 1):
        FirstPattern = Genome[i - 1:i - 1 + k]
        index = my_bf.PatternToNumber(FirstPattern)
        FrequencyArray[index] = FrequencyArray[index] - 1
        LastPattern = Genome[i + L - k: i + L]
        index = my_bf.PatternToNumber(LastPattern)
        FrequencyArray[index] = FrequencyArray[index] + 1
        if FrequencyArray[index] >= t:
            Clump[index] = 1

    for i in range(0, 4**k):
        if Clump[i] == 1:
            Pattern = my_bf.NumberToPattern(i,k)
            FrequentPatterns.append(Pattern)
    return FrequentPatterns

#print(*BetterClumpFinding(Genome, k, t, L))