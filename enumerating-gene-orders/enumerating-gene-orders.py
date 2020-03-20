'''


Problem:
http://rosalind.info/problems/perm/


'''


#Problem is relatively easy, and here is my naive implementation. As best at it could be optimized provided my current Python knowledge.

from itertools import permutations

with open('enumerating-gene-orders.txt') as FILE:
    READ_FILE = int(FILE.read())

def dna_permutations(NUMBER_OF_ELEMENTS = 3):

    '''
        Given a positive integer n≤7 returns the total number of permutations of length n, followed by a lists of all such permutations (in any order).
        >>>dna_permutations(3)
        >>>(6, [(1, 2, 3), (1, 3, 2), (2, 1, 3), (2, 3, 1), (3, 1, 2), (3, 2, 1)])
    '''

    #Generate list of integers to be permutated
    HELPING_LIST = [NUMBER+1
                    for NUMBER in range(NUMBER_OF_ELEMENTS)]

    #Generate list that will hold all the possible permutations
    PERMUTATION_LIST = []

    for PERMUTATION in permutations(HELPING_LIST):
        PERMUTATION_LIST.append(PERMUTATION)

    return len(PERMUTATION_LIST), PERMUTATION_LIST

print(dna_permutations())
