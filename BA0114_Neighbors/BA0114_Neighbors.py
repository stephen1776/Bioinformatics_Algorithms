'''
Generate the d-Neighborhood of a String

Find all the neighbors of a pattern.

Given: A DNA string Pattern and an integer d.

Return: The collection of strings Neighbors(Pattern, d).
Sample Dataset

ACG
1

Sample Output

CCG
TCG
GCG
AAG
ATG
AGG
ACA
ACC
ACT
ACG


'''

import sys, BA0107_HammingDistance as hd

def Neighbors(Pattern, d):
    if d == 0:
        return Pattern
    if len(Pattern) == 1:
        return ['A','C','G','T']
    Neighborhood = []
    suffixNeighbors = Neighbors(Pattern[1:], d)
    for Text in suffixNeighbors:
        if hd.HammingDistance(Pattern[1:], Text) < d:
            for x in ['A','C','G','T']:
                Neighborhood.append(x + Text)
        else:
            Neighborhood.append(Pattern[:1] + Text)
    #Neighborhood = list(set(Neighborhood))
    return Neighborhood


if __name__ == '__main__':
    infile = open('', 'r')
    lines = infile.read().splitlines()
    Pattern = lines[0]
    d = int(lines[1])
    infile.close()
    outFile = open("output/output_Neighbors.txt", "w")
    outFile.write('\n'.join(Neighbors(Pattern, d)))
    outFile.close()
    print(*Neighbors(Pattern, d))