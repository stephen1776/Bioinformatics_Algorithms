'''
Minimum Skew
Find a position in a genome minimizing the skew.

Given: A DNA string Genome.
Return: All integer(s) i minimizing Skew(Prefixi (Text)) over all values of i (from 0 to |Genome|).
'''
# Stephen Blatti 08042017
import sys
infile = open('', 'r')
lines = infile.read().splitlines()
Genome = lines[0]
infile.close()

def skew(Genome):
    skew = {}
    skew[0] = 0  # then define skew[i] = totalNum(G) - totalNum(C) in first i nucleotides of Genome
    for i in range(0, len(Genome)):
        if Genome[i] == 'G':
            skew[i + 1] = skew[i] + 1 # we can compute skew[i+1] from skew[i]
        elif Genome[i] == 'C':
            skew[i + 1] = skew[i] - 1
        else:
            skew[i + 1] = skew[i]
    return skew

def minimumSkew(Genome):
    minSkew = []
    s = skew(Genome)
    mval = min(s.values())
    for (k, v) in s.items():
        if v == mval:
            minSkew.append(k)
    return minSkew


print(*minimumSkew(Genome))
