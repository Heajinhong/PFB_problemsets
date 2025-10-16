#!/usr/bin/env python3

data = ['ATGCCCGGCCCGGC','GCGTGCTAGCAATACGATAAACCGG', 'ATATATATCGAT','ATGGGCCC']
# for m in data:
#     print(f'{len(m)}\t{m}')

# for m in data:
#     print(f'{data.index(m)}\t{len(m)}\t{m}\n')

print(sorted(data, key=len, reverse=True))