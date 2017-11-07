'''
Median String Problem

Find a median string.

Given: An integer k and a collection of strings Dna.

Return: A k-mer Pattern that minimizes d(Pattern, Dna) over all k-mers Pattern.
'''
import sys, HelperFunctions as hf

def  median_string(dna, k):
    distance = float('inf')
    for i in range(0,4**k):
        pattern = hf.NumberToPattern(i,k)
        if distance > hf.distanceBetweenPatternAndStrings(pattern, dna):
            distance = hf.distanceBetweenPatternAndStrings(pattern, dna)
            median = pattern
    return median


if __name__ == '__main__':
    infile = open('data/rosalind_ba2b2.txt', 'r')
    lines = infile.read().splitlines()
    k = int(lines[0])
    dna = lines[1:]
    infile.close()
    print(median_string(dna,k).replace(" ",""))