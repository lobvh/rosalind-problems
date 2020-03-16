'''

Problem:
http://rosalind.info/problems/subs/

'''


'''

DRAFT:

with open('finding-a-motif-in-dna_data.txt') as f:
    for line in f:
        print(line)
        print("---")
        
        
 for CHAR in DNA_STRING:
    if CHAR == DNA_SUBSTRING[0]:
        #Ovdje bi trebao pustiti for da odradi od pozicije gdje je sada CHAR na jos 4 pozicije dalje pa kad to zavrsi da se vrati na svoj prvobitni CHAR
'''


DNA_STRING = 'GATATATGCATATACTT'
DNA_SUBSTRING = 'ATAT'

'''
Naive solution V1:
- Take first letter of DNA_SUBSTRING
- Go trough each letter of a DNA_STRING and search for that first letter in DNA_SUBSTRING
    - This is gonna be a 'trigger'
- Check if next few letters form DNA_SUBSTRING 
    - When you encounter 'trigger' make dynamic list of next few letters and check if it is equal as DNA_SUBSTRING
    - Flush the helping_list
'''

#Naive solution V2 (using some of the ideas from V1!)

for POSITION, CHAR in enumerate(DNA_STRING):
    if CHAR == DNA_SUBSTRING[0] and DNA_STRING[POSITION:POSITION+4] == DNA_SUBSTRING:
        #print(POSITION+1)
        pass


#Solution V2 could be improved by using a bit more 'pythonic' wae:

DNA_STRING = 'GATATATGCATATACTT'
DNA_SUBSTRING = 'ATAT'

for POSITION in range(len(DNA_STRING)):
    if DNA_STRING.startswith(DNA_SUBSTRING, POSITION):
        print(POSITION+1)

''' 
if DNA_STRING.startswith(DNA_SUBSTRING, POSITION):
    print(POSITION+1)

"If DNA_STRING starts with the DNA_SUBSTRING on a position POSITION, return to me POSITION+1"

'''