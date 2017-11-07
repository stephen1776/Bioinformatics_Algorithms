'''
Compute DistanceBetweenPatternAndStrings

Find the distance between a pattern and a set of strings.

Given: A DNA string Pattern and a collection of DNA strings Dna.

Return: DistanceBetweenPatternAndStrings(Pattern, Dna).
'''
# Sample data
#pattern = 'AAA'
#strings = ['TTACCTTAAC','GATATCTGTC','ACGGCGTTCG','CCCTAAAGAG','CGTCAGAGGT']
#output = 5
import HelperFunctions as hf

def distanceBetweenPatternAndStrings(pattern, dna):
    k = len(pattern)
    distance = 0
    for string in dna:
        hamming_dist = float('Inf')
        for i in range(len(string) - k + 1):
            kmer = string[i:i+k]
            hd = hf.HammingDistance(pattern, kmer)
            if hamming_dist > hd:
                hamming_dist = hd
        distance += hamming_dist
    return distance


if __name__ == '__main__':

    infile = open('data/rosalind_ba2h.txt', 'r')
    lines = infile.read().splitlines()
    pattern = lines[0]
    strings = lines[1].split(' ')
    infile.close()
    print(distanceBetweenPatternAndStrings(pattern, strings))