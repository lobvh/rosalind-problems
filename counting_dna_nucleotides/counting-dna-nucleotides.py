'''

A string is simply an ordered collection of symbols selected from some alphabet and formed into a word; the length of a string is the number of symbols that it contains.

An example of a length 21 DNA string (whose alphabet contains the symbols 'A', 'C', 'G', and 'T') is "ATGCTTCAGAAAGGTCTTACG."

Given: A DNA string of length at most 1000 nt.

Return: Four integers (separated by spaces) counting the respective number of times that the symbols 'A', 'C', 'G', and 'T' occur in
.
'''

from collections import defaultdict

with open('rosalind_dna.txt') as f:
    read_data = f.read()

def dna_string_symbol_counter(dna_string = read_data):
    '''
        Given a DNA string return count of each letter in a string. DNA string consists of 4 symbols 'A','C','G' and 'T'.

        Example:
            dna_string = "AGCTTTTCATTCTGACTGCAACGGGCAATATGTCTCTGTGTGGATTAAAAAAAGAGTGTCTGATAGCAGC"
        >>> dna_string_symbol_counter(dna_string)
        >>> 20 17 12 21
    '''

    dict_letter_counter = defaultdict(int)

    for character in dna_string:
        dict_letter_counter[character] += 1

    a, c, g, t = dict(dict_letter_counter).values()

    return a,c,g,t

print(dna_string_symbol_counter())