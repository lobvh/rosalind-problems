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

from itertools import combinations
from collections import defaultdict

HELPING_STRING = "GORAN"
DNA_STRINGS = ['GATTACA', 'TAGACCA', 'ATACA']

def strings_to_substrings(strings=HELPING_STRING):

    '''
        Converts a DNA string into all combinations of motifs it can make. Returns a dictionary where keys represent DNA strings, and values represent
        list of all possible motifs.
        >>>DNA_STRINGS = "GORAN"
        >>>dna_string_to_motifs(DNA_STRINGS)
        >>>{'GORAN': ['GO', 'GOR', 'GORA', 'GORAN', 'OR', 'ORA', 'ORAN', 'RA', 'RAN', 'AN']}

    '''

    #First line of defense if someone invokes this function using string as an input:

    temporary_list = [element
                      for element in strings]
    strings_to_substrings_dict = defaultdict(list)


    for each_string in temporary_list:

        all_combinations_of_substrings = [each_string[range_start:range_end]
                                          for range_start, range_end in combinations(range(len(each_string) + 1), r=2)]
        substrings_of_size_2_and_more = [substring
                                         for substring in all_combinations_of_substrings
                                         if len(substring) > 1]
        strings_to_substrings_dict[each_string] = substrings_of_size_2_and_more

    return dict(strings_to_substrings_dict)

#print(strings_to_substrings(DNA_STRINGS))

def longest_common_motif(data = DNA_STRINGS):

    '''
        Counts the number of motif occurencies in a given set of strings. Returns most common motif (motif with highest number of counts).
        >>> DNA_STRINGS = ['GATTACA', 'TAGACCA', 'ATACA']
        >>> longest_common_motif(DNA_STRINGS)
        >>> ('TA', 8)
    '''

    data_preprocessed = strings_to_substrings(data)
    counting_dict = defaultdict(int)

    #Accesing necessary elements for comparison
    for each_element in data:
        for value in data_preprocessed.values():
            list_of_substrings = value
            for substring in list_of_substrings:
                if substring in each_element:
                    counting_dict[substring] += 1

    helping_dict = dict(counting_dict)

    #Since we counted substrings in their own strings we have to -1 each count
    helping_dict_refined = helping_dict

    for key in helping_dict.keys():
        helping_dict_refined[key] -= 1

    max_occurent_motif = max(helping_dict_refined, key=helping_dict_refined.get)
    return max_occurent_motif, helping_dict_refined[max_occurent_motif]


#print(longest_common_motif())


##### Let's manage our .txt file :

with open('finding-a-shared-motif.txt') as txt_file:

    #Read all the lines from raw file
    read_data = txt_file.readlines()

    #Strip \n's from the raw_file
    read_data = [element.strip("\n")
                            for element in read_data]

    #Make a dictionary out of it where keys represent >Rosalind_xxxx and it's values corresponding DNA strings that were previously divided
    read_data_dict = defaultdict(str)
    for element in read_data:

        if element.startswith(">"):
            current_element = element
            read_data_dict[current_element] = ""
        else:
            read_data_dict[current_element] += element

    #read_data_dict = dict(read_data_dict) <- We are not gonna do this for memory savings. It is better to stay as iterable because of the next thing I should do!

#Since we don't need names of FASTAs, we are gonna make a list out of values in read_data_dict. It's also appropriate data type to feed our functions!

data_string_list = []

for value in read_data_dict.values():
    data_string_list.append(value)

print(data_string_list)

data_substrings_dictionary = strings_to_substrings(data_string_list)

datas_longest_motif = longest_common_motif(data_substrings_dictionary)



print(datas_longest_motif)







