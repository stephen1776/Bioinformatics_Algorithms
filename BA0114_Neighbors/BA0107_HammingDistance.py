'''
Hamming Distance Problem
Compute the Hamming distance between two DNA strings.

Given: Two DNA strings.
Return: An integer value representing the Hamming distance.
'''
# Stephen Blatti 08052017

def HammingDistance(DNA1, DNA2):
    hamDist = [0]
    if len(DNA1) != len(DNA2):
        raise ValueError("Undefined for sequences of unequal length")
    for i in range(0, len(DNA1)):
        hamDist = sum(u != v for u,v in zip(DNA1, DNA2))
    return hamDist



if __name__ == '__main__':
    infile = open('', 'r')
    lines = infile.read().splitlines()
    DNA1 = lines[0]
    DNA2 = lines[1]
    infile.close()
    print(HammingDistance(DNA1, DNA2))
