#!/usr/bin/env python3
def rev_comp(dna):
    dna = dna.lower()
    dna1 = dna.replace('a', "T")
    dna2 = dna1.replace('t','A')
    dna3 = dna2.replace('c','G')
    dna4 = dna3.replace('g','C')
    dna5 = dna4[::-1]
    return(dna5)

dna = 'CGTGCTTTCCACGACGGTGACACGCTTCCCTGGA'
dna_rev = rev_comp(dna)
print(f'The reverse complement sequence is {dna_rev}')
