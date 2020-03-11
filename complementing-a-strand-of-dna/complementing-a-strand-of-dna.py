'''


In DNA strings, symbols 'A' and 'T' are complements of each other, as are 'C' and 'G'.

The reverse complement of a DNA string s is the string s^c formed by reversing the symbols of s, then taking the complement of each symbol
(e.g., the reverse complement of "GTCA" is "TGAC").

Given: A DNA string s of length at most 1000 bp.

Return: The reverse complement s^c of s.


SAMPLE DATASET: AAAACCCGGT
SAMPLE OUTPUT: ACCGGGTTTT

'''


######## More readable version #######

'''
Since doing succesive filtering using replace() has problems because the way the function is implemented, one can
use "replacing-with-the-lowercase-letter" trick, and then after everything is 'replaced' put it all to upper!
What an elegant solution! 
'''
sample_dna = 'AAAACCCGGT'

def complementing_dna(sample = sample_dna):

    sample_dna_reversed = "".join(list(reversed(sample)))
    reversed_dna_complemented = sample_dna_reversed.replace('A', 't').replace('T', 'a').replace('G', 'c').replace('C', 'g').upper()

    return reversed_dna_complemented

print(complementing_dna())

def complementing_dna():
    pass