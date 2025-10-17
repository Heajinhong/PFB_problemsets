#!/usr/bin/env python3
myset = set()
myset2 = {}
mySet = set('ATGTGGG')
mySet2 = {'ATGTGGG'}
#Question1 
#the difference is that set does not have any values. Just keys. Also, it is unordered, and no duplicates. 
#yes it matters which method you use. 
#in both, there are one item each

#Question 2
set1 = {'3','14','15','9','26','5','35','9'}
set2 = {'60','22','14','0','9'}
print(f'the difference set is {set1 - set2}') # this is difference
print(f'the intersection of the set is {set1&set2}') #this is intersection
print(f'the union set is {set1|set2}')
print(f'the symmetric difference is {set1^set2}') #this is symmetric difference
