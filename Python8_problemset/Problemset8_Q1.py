#!/usr/bin/env python3
import re
fasta = {}
seq = ''
with open("Python_08.fasta.txt","r") as fasta_read:
    for line in fasta_read:
        line = line.rstrip()      
        if line.startswith('>'):
            #store in a variable up to the ID
            #else, skip to the next line.
            seqName = re.search(r"(>.\S+)\s(.+)", line)
            seqName = seqName.group(1)
            seqName = seqName.replace('>','')
            fasta[seqName] = ''    
            nts = {}            
        else: 
            for nt in line:
                if nt in nts:
                    nts[nt] += 1
                else:
                    nts[nt] = 1    
            fasta[seqName] = nts
print(fasta)