#!/usr/bin/env python3
import Bio
from Bio import SeqIO
from Bio.SeqUtils import gc_fraction  ##use Bio.SeqUtils gc_fraction function to calculate it
dict ={}
gc_dict = {}
seq_list = []
total_len = 0
for seq_record in SeqIO.parse("/Users/pfb/PFB_problemsets/Biopython/Python_08.fasta", "fasta"):
    sequence = seq_record.seq
    sequence = str(sequence)
    id = seq_record.id
    dict[id] = sequence
    nt_number = len(sequence)
    total_len += nt_number
    seq_list.append(sequence)
    gc_dict[id] = f'{gc_fraction(seq_record):.1%}'
sorted_seq = sorted(seq_list, key=len, reverse=False)
GC_list = []
for seq in sorted_seq:
    G = seq.count('G')
    C = seq.count('C')
    length = len(seq)
    GC_cont = (G+C)/length
    GC_list.append(GC_cont)
print(GC_list)

print(type(sequence))
print(f'sequence count: {len(dict)}')
print(f'total number of nucleotides: {total_len}')
print(f'avg len: {total_len/(len(dict))}')
print(f'shortest len: {sorted_seq[0]}')
print(f'longest len: {sorted_seq[-1]}')
print(f'avg GC content: {(sum(GC_list))/(len(dict)):.1%}')
print(f'lowest GC content: {min(GC_list):.1%}')
print(f'highest GC content: {max(GC_list):.1%}')
print(f'{gc_dict}')