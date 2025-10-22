#!/usr/bin/env python3
import random 
seq = 'ABCD'
y = list(seq)
for x in range(len(seq)):
    positionA = random.randrange(0, len(seq)) 
    positionB = random.randrange(0, len(seq))

    value_posA = y[positionA]
    value_posB = y[positionB]
    y[positionA] = value_posB
    y[positionB] = value_posA
    print(positionA, positionB, y)

final = ''.join(y)
print(final)