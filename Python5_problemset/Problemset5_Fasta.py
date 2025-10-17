#!/usr/bin/env python3
fasta = {}
with open("Python_06.fasta","r") as seq_read:
    for line in seq_read:
        line = line.rstrip()
        if line.startswith('>'):
            geneID = line
            geneID = geneID.replace('>','')
            fasta[geneID] = ''
        else:
            seq = line
            fasta[geneID]+= seq
print(fasta)

        