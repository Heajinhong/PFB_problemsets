#!/usr/bin/env python3

##Question5 : Create a new function that calculates the GC content of a DNA sequence.
##it will take a DNA sequence without spaces and no header as an argument and return the percentage of nucleotides that are a G or C.
def GC_content(dna):
    nts = {}
    for nt in dna:
        if nt in nts:
            nts[nt] += 1
        else:
            nts[nt] = 1
    G = nts['G']
    C = nts['C']
    T = nts['T']
    A = nts['A']
    GC_cont = (G+C)/(G+C+T+A)
    return GC_cont

dna = 'CGTGCTTTCCACGACGGTGACACGCTTCCCTGGA'
GC_cont = GC_content(dna)
print(f'Percent GC content is {GC_cont:.1%}') 