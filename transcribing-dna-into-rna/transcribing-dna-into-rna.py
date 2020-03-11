'''

Problem

An RNA string is a string formed from the alphabet containing 'A', 'C', 'G', and 'U'.

Given a DNA string t corresponding to a coding strand, its transcribed RNA string u  is formed by replacing all occurrences of 'T' in t with 'U' in u

Given: A DNA string t having length at most 1000 nt.

Return: The transcribed RNA string of t.

SAMPLE: GATGGAACTTGACTACGTAAATT
OUTPUT: GAUGGAACUUGACUACGUAAAUU
'''


from datetime import datetime

with open('rosalind_rna.txt') as f:
    read_data = f.read()

#####
start_time = datetime.now()
#####

sample_dna = 'GATGGAACTTGACTACGTAAATTGATGGAACTTGACTACGTAAATTGATGGAACTTGACTACGTAAATTGATGGAACTTGACTACGTAAATTGATGGAACTTGACTACGTAAATT'

def dna_to_rna(sample = sample_dna):
    for character in sample:
       if character == 'T':
           yield 'U'
       else:
           yield character

dna_to_rna_gen = dna_to_rna(read_data)

helping_list = []

for each_element in dna_to_rna_gen:
        helping_list.append(each_element)

print("".join(helping_list))

#####
end_time = datetime.now()
print('Duration of the first one: {}'.format(end_time - start_time))
#####


########### More Pythonic wae? ###########

#####
start_time = datetime.now()
#####


sample_dna_1 = read_data
sample_dna_1 = read_data.replace("T", "U")
print(sample_dna_1)

#####
end_time = datetime.now()
print('Duration of the second one: {}'.format(end_time - start_time))
#####

#If we keep increasing the "sample size" second implementation is around on average 3 times faster than first one!
#I learned something new today, yay!


with open("converted_rna.txt", 'w') as f:
    write_data = f.write(sample_dna_1)
