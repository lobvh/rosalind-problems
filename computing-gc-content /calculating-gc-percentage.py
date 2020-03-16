'''

Problem:
http://rosalind.info/problems/gc/

'''

from datetime import datetime
from collections import defaultdict

sample_1= ['>Rosalind_6404 CCTGCGGAAGATCGGCACTAGAATAGCCAGAACCGTTTCTCTGAGGCTTCCGGCCTTCCCTCCCACTAATAATTCTGAGG',
          '>Rosalind_5959 CCATCGGTAGCGCATCCTTAGTCCAATTAAGTCCCTATCCAGGCGCTCCGCCGAAGGTCTATATCCATTTGTCAGCAGACACGC',
          '>Rosalind_0808 CCACCCTCGTGGTATGGCTAGGCATTCAGGAACCGGAGAACGCTTCAGACCAGCCCGGACTGGGAACCTGCGGGCAGTAGGTGGAAT']

def highest_gc_content(data = sample_1):
    '''
        Calculates the GC-content of DNA string array in FASTA format.
        Returns the ID of the string having the highest GC-content, followed by the GC-content of that string.

        >>> data = ['>Rosalind_6404 CCTGCGGAAGATCGGCACTAGAATAGCCAGAACCGTTTCTCTGAGGCTTCCGGCCTTCCCTCCCACTAATAATTCTGAGG',
          '>Rosalind_5959 CCATCGGTAGCGCATCCTTAGTCCAATTAAGTCCCTATCCAGGCGCTCCGCCGAAGGTCTATATCCATTTGTCAGCAGACACGC',
          '>Rosalind_0808 CCACCCTCGTGGTATGGCTAGGCATTCAGGAACCGGAGAACGCTTCAGACCAGCCCGGACTGGGAACCTGCGGGCAGTAGGTGGAAT']
        >>> highest_gc_content(data)
        >>> Rosalind_0808 60.919540
    '''

    pass




##### V1


#####
start_time = datetime.now()
#####


sample_0808 = 'CCACCCTCGTGGTATGGCTAGGCATTCAGGAACCGGAGAACGCTTCAGACCAGCCCGGACTGGGAACCTGCGGGCAGTAGGTGGAAT'
count = 0
for char in sample_0808:
    if char == "C" or char == "G":
        count += 1
gc_percentage = (count/len(sample_0808))*100
gc_percentage_string = "GC percentage using 6 significant digits {:.6f}".format(gc_percentage)
#print(gc_percentage_string)


#####
end_time = datetime.now()
#print('Duration of the V1: {}'.format(end_time - start_time))
#####




##### V2 'drop unnecessary information'

#####
start_time = datetime.now()
#####

s = 'CCACCCTCGTGGTATGGCTAGGCATTCAGGAACCGGAGAACGCTTCAGACCAGCCCGGACTGGGAACCTGCGGGCAGTAGGTGGAAT'
s_filtered = "".join(sorted(s))
s_striped = len(s_filtered.strip("A").strip("T")) #strip() strips leading or trailing strings
gc_percentage = (s_striped/len(s))*100
gc_percentage_string = "GC percentage using 6 significant digits {:.6f}".format(gc_percentage)
#print(gc_percentage_string)


#####
end_time = datetime.now()
#print('Duration of the V1: {}'.format(end_time - start_time))
#####







###### Making dictionary for each sample
'''
'>Rosalind_6404 CCTGCGGAAGATCGGCACTAGAATAGCCAGAACCGTTTCTCTGAGGCTTCCGGCCTTCCCTCCCACTAATAATTCTGAGG'

Make key value pairs where {'>Rosalind_6404':GC percentage of rosalind_6404} is key, value pair

'''

with open('rosalind_dna.txt') as f:
    read_data = f.read()

read_data_s = read_data.split("\n")
#print(read_data_s)


def gc_percentage_calculator(data, percentage_or_not=True):
    '''
        By default returns the GC percentage of a given string.
        Additionally, if you set the percentage_or_not to False it returns tuple where first number indicates the number of G's and C's in a given string, and second one length of a given string.

        >>> data = 'TGACCGAAGAGCTCCCACGCCACCAGCCTAAAGACTTGGAGGGATCGCAGACCTCCAAGA'
        >>> gc_percentage(data)
        >>> 40.229885057471265
    '''

    #Sort the data alphabeticaly...
    data_sorted = "".join(sorted(data))

    #... so that we can strip the unnecesarry content (A's and T's),
    data_striped = data_sorted.strip("A").strip("T")

    if percentage_or_not:
        return (len(data_striped) / len(s)) * 100
    else:
        return len(data_striped), len(data)



helping_dictionary = defaultdict(list) # Could use tuple instead of list to save more memory...

#We are gonna use "the trigger trick" here, because we need to keep track of each '>Rosalind_xxx' values.
for value in read_data_s:

    #First we 'capture' the '>Rosalind_xxxx' for our key in dictionary:
    if value.startswith('>'):
        current_value = value
        helping_dictionary[current_value] = [0, 0]

    #And then we update it's values until the if get's 'triggered' by the next '>Rosalind_xxxx' value
    else:
        a, b = gc_percentage_calculator(value, False)
        helping_dictionary[current_value][0] += a
        helping_dictionary[current_value][1] += b

#print(dict(helping_dictionary))


#Make dictionary of percentages:
percentage_dictionary = defaultdict(int)

for key, value in helping_dictionary.items():
    percentage_dictionary[key] = round((value[0]/value[1])*100, 6)

#print(dict(percentage_dictionary))

#Reverse key/value pairs, so it's easy to get name of '>Rosalind_xxx' which has highest percentage:

percentage_dictionary = dict(percentage_dictionary)
percentage_dictionary_reversed = {value : key
                                  for key, value in percentage_dictionary.items()}

#Make empty list so we can obtain max percentage
helping_list = []

for value in dict(percentage_dictionary).values():
    helping_list.append(value)

print("'>Rosalind_xxx' with maximum GC percentage is '{}' with {}%".format(percentage_dictionary_reversed[max(helping_list)], max(helping_list)))


'''
Learned:
- "Trigger trick"
- Could improve code
- Applied some new skills learned (unpacking tuples, changing key/value pairs etc.)
'''