#!/usr/bin/env python3
name = "HeaJin"
print(f"My name: {name}")
print('My favorite color: Lavender')
hobby = "video games"
print("My favorite activity:", hobby)
animal = "cat"
animal_name = "(Kong)"
print("My favorite animal:", animal, animal_name)

import sys

name = sys.argv[1]
favorite_color = sys.argv[2]
favorite_animal = sys.argv[3]
print("My name is", name, "my favorite color is", favorite_color, 'and', 'my favorite animal is', favorite_animal)

