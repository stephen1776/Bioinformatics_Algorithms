'''
Implanted Motif Problem
Implement MotifEnumeration (shown above) to find all (k, d)-motifs in a collection of strings.

Given: Integers k and d, followed by a collection of strings Dna.
Return: All (k, d)-motifs in Dna.
'''
import HelperFunctions as hf

def motifEnumeration(DNAs, k, d):
    patterns = dict()
    for dna in DNAs:
        patterns[dna] = set()
        for i in range(len(dna) - k + 1):
            patternPrime = dna[i:i + k]
            patterns[dna] = patterns[dna].union(hf.Neighbors(patternPrime, d))
    motifs = patterns.values()
    ''' remove duplicates '''
    return(set.intersection(*motifs))


if __name__ == '__main__':
    infile = open('../data/sample_motifEnumeration.txt', 'r')
    lines = infile.read().splitlines()
    k = int(lines[0].split(' ')[0])
    d = int(lines[0].split(' ')[1])
    DNAs = lines[1:]
    print(*motifEnumeration(DNAs, k, d))
