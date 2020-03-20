'''


Problem:
http://rosalind.info/problems/lcsm/


Sample dataset:

>Rosalind_1
GATTACA
>Rosalind_2
TAGACCA
>Rosalind_3
ATACA

Sample output
AC
'''

####Scrible code... Initial estimations

# I will hold everything in a list since 'If multiple solutions exist, you may return any single solution.', and I can use max() with key=len on that list.

lista_stringova = ["Bla", "KRAS", "JAPAAR"]

# print(len(max(lista_stringova, key=len)))

HELPING_LIST = []
if "MOTIF" in 'EACH_DATA_STRING':
    pass

'''
- Minimum size of a motif is 2
- Make a list of substrings from one >Rosalind_x and treat everything else as a strings to search through them
- Since each DNA string can possibly be different sizes check also if full DNA string is included
'''
from collections import defaultdict

DNA_STRINGS = ['GATTACA', 'TAGACCA', 'ATACA']

DNA_SUBSTRINGS_DICT = defaultdict(list)

for ELEMENT in DNA_STRINGS:
    CURRENT_MOTIF_SAMPLE = ELEMENT
    #Creates a list of substrings of current motif sample
    MOTIF_SAMPLE_SUBSTRINGS = []
    for NUMBER in range(len(CURRENT_MOTIF_SAMPLE) + 1):
        if NUMBER > 1:
            DNA_SUBSTRINGS_DICT[CURRENT_MOTIF_SAMPLE].append(CURRENT_MOTIF_SAMPLE[0:NUMBER])

print(dict(DNA_SUBSTRINGS_DICT))

#Checking if there is a motif in other DNA strings
