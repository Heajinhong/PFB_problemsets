#!/usr/bin/env python3
kong = 60
if kong%2 == 0:
    print(kong,'is even')
    if kong > 0:
        print(kong, 'is positive')
        if kong < 50:
            print(kong, 'is smaller than 50')
            if kong%2 == 0:
                print(kong, 'is an even number that is smaller than 50')
        elif kong == 50:
            print(kong, 'is equal to 50')
        elif kong > 50:
            print(kong, 'is greater than 50')
            if kong%3 == 0:
                print(kong, 'is larger than 50 and divisible by 3')
            else:
                print(kong, 'is larger than 50 but not divisible by 3')
    else:
        print(kong, 'is negative')
elif kong == 0:
    print(kong, 'is zero')
else:
    print(kong,'is odd')
