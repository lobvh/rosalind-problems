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

#I will hold everything in a list since 'If multiple solutions exist, you may return any single solution.', and I can use max() with key=len on that list.

lista_stringova = ["Bla", "KRAS", "JAPAAR"]

print(len(max(lista_stringova, key=len)))

HELPING_LIST = []
if "MOTIF" in EACH_DATA_STRING:

