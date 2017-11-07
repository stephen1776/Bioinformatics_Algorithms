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

def distanceBetweenPatternAndString(pattern, text):
    ham_distance = float('inf')
    for i in range(len(text) - len(pattern) + 1):
        hd = hf.HammingDistance(pattern, text[i:i + len(pattern)])
        if hd < ham_distance:
            ham_distance = hd
    return ham_distance


def distanceBetweenPatternAndStrings(pattern, strings):
    k = len(pattern)
    distance = 0
    for i in range(len(strings)):
        distance += distanceBetweenPatternAndString(pattern, strings[i])
    return distance



if __name__ == '__main__':

    infile = open('data/rosalind_ba2h.txt', 'r')
    lines = infile.read().splitlines()
    pattern = lines[0]
    strings = lines[1].split(' ')
    infile.close()
    print(distanceBetweenPatternAndStrings(pattern, strings))