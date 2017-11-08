'''
Profile-most Probable k-mer Problem

Find a Profile-most probable k-mer in a string.

Given: A string Text, an integer k, and a 4 × k matrix Profile.

Return: A Profile-most probable k-mer in Text.
'''

import os, numpy as np

def profileMostProbableKmer(seq, k, profile):
    nucleoToInt = {'A':0,'C':1,'G':2,'T':3}
    bestp = float('-inf')
    best = None
    for i in range(len(seq)-k+1):
        kmer = seq[i:i + k]
        prob = 1
        for ki in range(len(kmer)):
          prob = prob * profile[nucleoToInt[kmer[ki]]][ki]
        if prob > bestp:
           best = kmer
           bestp = prob
    return best

if __name__ == '__main__':

    #seq = 'ACCTGTTTATTGCCTAAGTTCCGAACAAACCCAATATAGCCCGAGGGCCT'
    #k = 5
    #profile = np.asarray([[0.2, 0.2, 0.3, 0.2, 0.3],[0.4, 0.3, 0.1, 0.5, 0.1],[0.3, 0.3, 0.5, 0.2, 0.4],[0.1, 0.2, 0.1, 0.1, 0.2]])
    # sample output = CCGAG
    #seq = 'TGCCCGAGCTATCTTATGCGCATCGCATGCGGACCCTTCCCTAGGCTTGTCGCAAGCCATTATCCTGGGCGCTAGTTGCGCGAGTATTGTCAGACCTGATGACGCTGTAAGCTAGCGTGTTCAGCGGCGCGCAATGAGCGGTTTAGATCACAGAATCCTTTGGCGTATTCCTATCCGTTACATCACCTTCCTCACCCCTA'
    #k = 6
    #profile = np.asarray([[0.364,0.333,0.303,0.212,0.121,0.242],[0.182,0.182,0.212,0.303,0.182,0.303],[0.121,0.303,0.182,0.273,0.333,0.303],[0.333,0.182,0.303,0.212,0.364,0.152]])
    # sample2 output = TGTCGC

    seq = 'CCATCATAACAGTGCTCGTTAGACCCCGGTATTGTGTCTGGCGGTAGAGGTGATTGGAACATCGTCCCCCGGTCGCCATCCTAGTCCTAATATTCTTATCGTTACGTTACGAAATACTGCTGTAGCACTTGGGTCTATTATGGGCTGAGCGACCGAATCTGGCCACAGAACAGGAGGCCGCCCAAGTGTAGATATAGATC'
    k = 7
    profile = np.asarray([[0.214,0.321,0.214,0.179,0.25,0.071,0.357],[0.286,0.179,0.143,0.357,0.25,0.321,0.25],[0.321,0.179,0.536,0.25,0.25,0.179,0.107],[0.179,0.321,0.107,0.214,0.25,0.429,0.286]])
    #CTGGCCA
    kmers = profileMostProbableKmer(seq, k, profile)
    print(kmers)