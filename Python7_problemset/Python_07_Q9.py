#!/usr/bin/env python
import re
neb = {}
with open('neb_cutsites.txt','r') as seq_read:
    seq_read = seq_read.read()
    for found in re.finditer(r"(\S+.\S+)\s{2,}(\S+)", seq_read):
        enzyme = found.group(1)
        seq = found.group(2)
        neb[enzyme] = seq
print(neb)

#Question10
import sys
ez = sys.argv[1]
# with open('Python_07_Q10_fasta.txt','r') as to_cut:
#     fasta_read = to_cut.read()
#     seq = neb[ez]
for enzyme in neb:
    seq = neb[enzyme]
    if seq
