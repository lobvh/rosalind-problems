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

def dna_string_to_motifs(DNA_DATA = DNA_STRINGS):

    '''
        Converts a DNA string into all combinations of motifs it can make. Returns a dictionary where keys represent DNA strings, and values represent
        list of all possible motifs.
        >>>DNA_STRINGS = ['GATTACA', 'TAGACCA', 'ATACA']
        >>>dna_string_to_motifs(DNA_STRINGS)
        >>>{'GATTACA': ['GA', 'GAT', 'GATT', 'GATTA', 'GATTAC', 'GATTACA'], 'TAGACCA': ['TA', 'TAG', 'TAGA', 'TAGAC', 'TAGACC', 'TAGACCA'], 'ATACA': ['AT', 'ATA', 'ATAC', 'ATACA']}

    '''

    DNA_SUBSTRINGS_DICT = defaultdict(list)
    #For each element in a DNA_STRINGS creates a list of substrings ('sub-motifs').
    for ELEMENT in DNA_DATA:

        #These 'submotifs' can be of length 2 up-to length of an element because they have diferent length, and could be thus contained in each other.
        for NUMBER in range(len(ELEMENT) + 1):
            if NUMBER > 1:
                DNA_SUBSTRINGS_DICT[ELEMENT].append(ELEMENT[0:NUMBER])

    return dict(DNA_SUBSTRINGS_DICT)

'''
- Create a default dictionary where keys represent submotifs, and values represent number of times it occured
- Go trough all elements in DNA_STRINGS list where list[-1] != current_element (we do not want to count anything that is already in that element
- Switch to the next list in dictionary
- After finishing -1 each count (because of self-count!) 
'''

DNA_STRING_SUBMOTIFS_DICT = dna_string_to_motifs()

DNA_SUBMOTIFS_DICT = defaultdict(int)

for DICT_VALUE in DNA_STRING_SUBMOTIFS_DICT.values():
    CURRENT_LIST = DICT_VALUE
    for CURRENT_LIST_VALUE in CURRENT_LIST:
        for ELEMENT in DNA_STRINGS:
            if CURRENT_LIST_VALUE in ELEMENT:
                DNA_SUBMOTIFS_DICT[CURRENT_LIST_VALUE]+=1

#print(list(DNA_STRING_SUBMOTIFS_DICT.keys()))
#print(dict(DNA_SUBMOTIFS_DICT))

#########################I forgot to extract ATTAC, TTAC, TAC, AC etc. These also count as submotifs. ##########################

string_h = "GORAN"

#print(string_h[-5:5])

list_help = []

for position in reversed(range(2, len(string_h))):
    print(string_h[-position:len(string_h)])

#This needs to be implemented into function dna_string_to_motifs()






