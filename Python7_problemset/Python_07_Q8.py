#!/usr/bin/env python3
# import re
# with open('test2.txt','r') as seq_read:
#     seq_read = seq_read.read()
#     cut_site = re.search(r"(.+)\^(.+)\^(.+)", seq_read)
# upstream = cut_site.group(1)
# downstream = cut_site.group(2)
# downstream2 = cut_site.group(3)
# print(upstream)
# print(downstream)
# print(downstream2)
#no need to use regular expression. you can just split it
total_seq = ''
with open('ApoI_cutsites.txt','r') as seq_read:
    for line in seq_read:
        line = line.rstrip()
        if line.startswith('>'):
            continue
        total_seq += line
seq_read = total_seq.split('^')
seq_read = sorted(seq_read, key=len, reverse= True)
print(seq_read)