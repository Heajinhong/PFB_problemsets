#!/usr/bin/bash python3
#Question 1
favorites = {} # need to create an empty dictionary
favorites['book'] = 'Jitterbug Perfume' #dictionary['key'] = 'value'
favorites['song'] = "Tom Petty - I Won't Back Down" # have double quotations on the ones that wil have single quotation in a string.
favorites['tree'] = 'Cedar'
print(favorites)  

# #Question2
# print(favorites['book'])

# #Question3 
# fav_thing = 'book'
# print(favorites[fav_thing])

# #Question4
# fav_thing2 = 'tree'
# print(favorites[fav_thing2])

#Question5
favorites['organism'] = 'kong'
fav_thing3 = 'organism'
print(favorites[fav_thing3])

#Question6
for fav in favorites: 
    things = favorites[fav]
    print(f'{fav}: {things}')

#Question7
thing = favorites['organism']
print(thing)

#Question8
print('check out these things:')
for things in favorites:
    print(things)
#Question9
favorites['organism'] = 'boree'
things = input()
print(f'My favorite organism is{favorites['organism']}')