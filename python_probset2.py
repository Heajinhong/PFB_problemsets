#!/usr/bin/env python3
hello = 50
if hello != 'Aye Captain':
    print('Not True')
else:
    print('True')
if hello > 0:
    print('positive')
    if hello < 50:
        print(hello, 'is less than 50')
    else: 
        print(hello, 'is greater than 50 or equal to 50')
    if hello%2 == 0: 
        print(hello, 'is even')
    else:
        print(hello, 'is not even')
    if hello > 50 and hello%3 == 0:
        print(hello, 'is larger than 50 and divisible by 3') 
    else:
        print(hello, 'is not larger than 50 and/or not divisible by 3')
elif hello == 0:
    print('zero')
else:
    print('negative')
