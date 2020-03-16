'''

Problem:
http://rosalind.info/problems/hamm/

'''

SAMPLE_1 = 'GAGCCTACTAACGGGAT'
SAMPLE_2 = 'CATCGTAATGACGGCCT'

with open('hamming_distance_data.txt') as FILE:
    READ_DATA = FILE.read()

DATA_PREPROCESSED = READ_DATA.split('\n')

def hamming_distance(FIRST_DNA_STRING = SAMPLE_1, SECOND_DNA_STRING = SAMPLE_2):

    '''
        Calculates and returns "Hamming distance" between two DNA strings.
        By definition the Hamming distance between two strings is a number of mismatched symbols in two strings.

        >>> first_dna_string = 'GAGCCTACTAACGGGAT'
        >>> second_dna_string = 'CATCGTAATGACGGCCT'
        >>> hamming_distance(first_dna_string, second_dna_string)
        >>> 7
    '''

    HAMMING_DISTANCE = 0

    for CHAR_1, CHAR_2 in zip(FIRST_DNA_STRING, SECOND_DNA_STRING):
        if CHAR_1 != CHAR_2:
            HAMMING_DISTANCE += 1

    return HAMMING_DISTANCE

print(hamming_distance(DATA_PREPROCESSED[0],DATA_PREPROCESSED[1]))


