#!/usr/bin/env python3
import Bio
from Bio import SeqIO
filename = "/Users/pfb/PFB_problemsets/Biopython/uniprot_sprot.fasta"
text = open("s_paratyphi.prot.fa", "w")
for seq_record in SeqIO.parse(filename, "fasta"):
#    print(seq_record.description)
    ID = seq_record.description
    sequence = seq_record.seq
    if 'OS=Salmonella paratyphi B' in ID:
        #print(f'ID:{ID}\nsequence:{sequence}') 
        text.write(f'>{ID}\n{sequence}\n')
        #text.close()