#!/usr/bin/env python3
import re
with open("Python_07_ApoI.fasta","r") as seq_read:
    seq_read = seq_read.read()
    repl_seq1 = re.sub(r'AAATTC', 'A^AATTC', seq_read)
    repl_seq2 = re.sub(r'AAATTT', 'A^AATTT', repl_seq1)
    repl_seq3 = re.sub(r'GAATTT', 'G^AATTT', repl_seq2)
    repl_seq4 = re.sub(r'GAATTC', 'G^AATTC', repl_seq3)
print(repl_seq4)

print(len(re.findall(r"\^AATT", repl_seq4)))
cut_ApoI = open("ApoI_cutsites.txt", "w")
cut_ApoI.write(repl_seq4)