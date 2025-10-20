#!/usr/bin/env python3
#Question1
nobody_txt = open("Python_07_nobody.txt", "r")
contents = nobody_txt.read()
import re
found =  re.findall(r"Nobody", contents)
print(found)
print(f"Question1 = There are {len(found)} 'Nobody' occur in the text.")
nobody_txt.close()

