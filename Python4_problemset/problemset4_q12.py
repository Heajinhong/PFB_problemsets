#!/usr/bin/env python3
import sys
min = int(sys.argv[1])
max = int(sys.argv[2])+1

#all = list(range(min,max))
odd=[]
for m in range(min,max):
    if m%2!=0:
        odd.append(m)
print(odd)
