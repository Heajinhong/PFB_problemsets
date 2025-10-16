#!/usr/bin/env python3
with open("Python_06.seq.txt", "r") as seq_read, open("Python_06_rev.seq.txt","w") as seq_write:
    for line in seq_read:
        line = line.rstrip()
        gene_id,seq = line.split('\t')
        seq1 = seq.lower()
        seq2 = seq1.replace('a','T')
        seq3 = seq2.replace('t','A')
        seq4 = seq3.replace('c','G')
        seq5 = seq4.replace('g','C')
        seq6 = seq5[::-1]
        seq_write.write(f"{gene_id}\t{seq6}\n")
    seq_write.write(f"This is the reverse complement")
print(seq_write)