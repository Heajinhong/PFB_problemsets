#!/usr/bin/env python3
import Bio
from Bio import SeqIO
for seq_record in SeqIO.parse("Users/pfb/PFB_problemsets/Python10_problemset/Biopython/fasta_test.fa", "fasta"):
    print('sequence', seq_record.seq)