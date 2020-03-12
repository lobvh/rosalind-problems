'''


In DNA strings, symbols 'A' and 'T' are complements of each other, as are 'C' and 'G'.

The reverse complement of a DNA string s is the string s^c formed by reversing the symbols of s, then taking the complement of each symbol
(e.g., the reverse complement of "GTCA" is "TGAC").

Given: A DNA string s of length at most 1000 bp.

Return: The reverse complement s^c of s.


SAMPLE DATASET: AAAACCCGGT
SAMPLE OUTPUT: ACCGGGTTTT

'''

from datetime import datetime


#Importing necessary files
import_file_path = '/Users/goceovoono/Desktop/git_projects/rosalind-problems/complementing-a-strand-of-dna/rosalind_dna.txt'

with open(import_file_path) as f:
    read_data = f.read()

sample_dna = 'AAAACCCGGT'

######## More readable version #######


#####
start_time = datetime.now()
#####

def complementing_dna_v1(sample = sample_dna):

    sample_dna_reversed = "".join(list(reversed(sample)))
    reversed_dna_complemented = sample_dna_reversed.replace('A', 't').replace('T', 'a').replace('G', 'c').replace('C', 'g').upper()

    return reversed_dna_complemented

#print(complementing_dna_v1(read_data))

#####
end_time = datetime.now()
print('Duration of the V1: {}'.format(end_time - start_time))
#####


####### More efficient version ########

#####
start_time = datetime.now()
#####

def complementing_dna_v2(sample = sample_dna):

    sample_dna_reversed = sample[::-1]
    reversed_dna_complemented = sample_dna_reversed.replace('A', 't').replace('T', 'a').replace('G', 'c').replace('C', 'g').upper()

    return reversed_dna_complemented

#print(complementing_dna_v2(read_data))

#####
end_time = datetime.now()
print('Duration of the V2: {}'.format(end_time - start_time))
#####

converted_rna = complementing_dna_v2(read_data)

export_file_path = '/Users/goceovoono/Desktop/git_projects/rosalind-problems/complementing-a-strand-of-dna/converted_dna.txt'

with open(export_file_path, 'w') as f:
    write_data = f.write(converted_rna)

'''
Learned:
Since doing successive filtering using replace() has problems because the way the function is implemented, one can
use "replacing-with-the-lowercase-letter" trick, and then after everything is 'replaced' put it all back to upper-case!
What an elegant solution! 

This time I had to use absoulte path for the unknown reason... 
FIXED: Found out that I was saving it to the different folder with the same name.......... FUCK!
'''