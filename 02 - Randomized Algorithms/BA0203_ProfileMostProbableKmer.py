'''
Profile-most Probable k-mer Problem

Find a Profile-most probable k-mer in a string.

Given: A string Text, an integer k, and a 4 × k matrix Profile.

Return: A Profile-most probable k-mer in Text.
'''

import os, numpy as np

def profileMostProbableKmer(text,k,profile):
	xaxis = {'A':0,'C':1,'G':2,'T':3}
	maxprob = float('-inf')
	maxkmer = None
	for i in range(len(text)-k+1):
		kmer = text[i:i+k]
		prob = 1
		for ki in range(len(kmer)):
			prob = prob * profile[xaxis[kmer[ki]]][ki]
		if prob > maxprob:
			maxkmer = kmer
			maxprob = prob
	return maxkmer

if __name__ == '__main__':
    filename = 'data/prof_most_prob_kmer.txt'
    if os.path.isfile('data/prof_most_prob_kmer.txt') == True:
        with open(filename) as f:
            lines = f.read().splitlines()
            text = lines[0]
            k = int(lines[1])
            profile = list([map(float,l.split(' '))for l in lines[2:]] )
            kmers = profileMostProbableKmer(text, k, profile)
            print(kmers)
    else:
        text = 'ACCTGTTTATTGCCTAAGTTCCGAACAAACCCAATATAGCCCGAGGGCCT'
        k = 5
        profile = np.matrix([[0.2, 0.2, 0.3, 0.2, 0.3],[0.4, 0.3, 0.1, 0.5, 0.1],[0.3, 0.3, 0.5, 0.2, 0.4],[0.1, 0.2, 0.1, 0.1, 0.2]])
        # 0.2 0.2 0.3 0.2 0.3
        # 0.4 0.3 0.1 0.5 0.1
        # 0.3 0.3 0.5 0.2 0.4
        # 0.1 0.2 0.1 0.1 0.2
        kmers = profileMostProbableKmer(text,k,profile)
        print(kmers)