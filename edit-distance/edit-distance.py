'''

Problem:
http://rosalind.info/problems/edit/


Given two strings s and t (of possibly different lengths), the edit distance dE(s,t) is the minimum number of edit operations needed to transform
s into t, where an edit operation is defined as the substitution, insertion, or deletion of a single symbol.


Sample dataset:

>Rosalind_39
A = PLEASANTLY
>Rosalind_11
B = MEANLY

Sample output:
5

'''


'''
We are gonna start with 'sample dataset' to gain some insights, and then we are gonna gradually extend the problem for any given dataset. 

Facts:

V1:
- Since len(A)>len(B) it is sure that we have to delete len(A)-len(B) elements of A in order to have the same number of elements in B. 
 - Since deletion is not an only thing that edit distance depend, one naive solution is to brute force it:
    "Delete len(A)-len(B) elements from A. We are dealing with variations here, so we can delete len(A)!/[len(A)-(len(A)-len(B))]! unique and different elements from A."
    (I hope it's called variations, but anyhow it would just indicate how much time it will take to try excluding len(A)-len(B) letters.)
 - Or we could try: "out of len(A) elements of A choose len(B)". Will we get the same result and time complexity? Good mental excercise, but I don't have time...
- For each variation calculate number of mismatched elements. That is the number of substitutions we need in order to transform s into t.
- Maybe it's a better strategy which has also less time complexity to find in A all elements that are same as B. If we have all of them then distance = len(A)-len(B). 
  Else, the distance is number_of_deletions+number_of_insertions+number_of_substitutions
  A = PLEASANTLY
  B = MEANLY
  
V1/V2:
  From A we have {E, A, N, L, Y}. For the simplicity, let's lowercase those letters:
  A_lower = PleaSAnTly (Do I need to lowercase second A and L?)
  
  So, we need to delete ANY 4 elements (it doesn't matter at all which ones!) and... 
  A_lower_deletion = leany

V2/V3:
  This is a dead end, and it will yield more than 5 for the sample output.
  I thought that attention is to the "set of same letters". That's why I was concerned with *Do I need to lowercase second A and L?*
  
V3/V4:
- Lowercase each letter in A that is already in B.
 A_lower = PleaSanTly
- I think this is a problem that is out of my reach... For example we could tabulate B such that number represent distances between letters:
  (We are gonna exclude M and count it as "one insertion", but one might need more clever idea than that...)
  E, A = 0; E, N = 1; E, L = 2; E,Y = 3;
  EA, N = 0; EA, L = 1; EA, Y = 2; EA, NLY = 0, EA, LY = 1; EA, NL = 0
  etc. 
  One would probably need those calculations and combinations of them to calculate "Should we leave second A or first A?".
  Maybe one could use 'penalties' such as EANLY = 3, ANLY = 2, NLY = 1, LY = 0. 
  Maybe this is "the master condition" if we calculate in our case for each combination we should decide "how good we are".
  If we are for example watching "EANLY" then expect that we need extra 2 deletions or that is always the case?
  Maybe we should focus our attention to 'It's better to have Y, but much better if we have LY, but... and in the best scenario to have "EANLY"'
- Or maybe we should watch everything relative to "EANLY"? Fact: Every string is alphabetically ordered. 
  Intuitevely, to obtain such case we would need SA to get "EAN" and delete T to get "EANLY". Then all we need is to delete first L or P and change it to M.
  So, we are deleting 4 elements and changing 1. That's how we get 5. 
- If the letters in A could be random, then we have bigger problem. But I think that one should expect A and B to always be alphabetically. 
  We just need to find rules for that case only. 
  
  It would either take me too much time to think and solve this problem (which could be beneficial, no doubt!) or I can see how "inventor of the algorithm" approached it. 
  
'''