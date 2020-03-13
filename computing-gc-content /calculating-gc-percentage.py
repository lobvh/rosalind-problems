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

read_data = str(read_data)
read_data_s = read_data.split("\n")
print(read_data_s)


def gc_percentage_calculator(data):

    data_filtered = "".join(sorted(data))
    data_striped = len(data_filtered.strip("A").strip("T"))
    return (data_striped / len(s)) * 100


helping_dictionary = defaultdict(int)
for value in read_data_s:
    if value.startswith('>'):
        helping_dictionary[value] += 0
        current_value = value
    else:
        helping_dictionary[current_value] += gc_percentage_calculator(value)

#Bug of logical nature it gives percentage relative to each value. One should keep track of number of bits till you find next startswith('>')
print(helping_dictionary)