#!/usr/bin/env python3
#Question1: Create a DNA sequence class that will contain a sequence, its name, and it's organism of origin. Do this by creating an __init__ function.
class DNAseq(object):
    #define class attributes
    def __init__(self, sequence, gene_name, species_name):
        #Question2: Write some some lines of code, outside your class (in your main program) that sets the name, DNA sequence, and organism for a gene.
        self.sequence = sequence.upper()
        self.gene_name = gene_name
        self.species_name = species_name
    #Question4: Sequence length method
    ##a. Add a method to your class that calculates and returns the length of the sequence.
    def len_seq(self):
        length = len(self.sequence)
        return length
    #Question5: Nucleotide composition method
    ##a. Add in a method that calculates and returns the nucleotide composition.
    def nt_comp(self):
        nts={}
        for nt in self.sequence:
            if nt in nts:
                nts[nt] += 1
            else:
                nts[nt] = 1
        if 'G' not in nts.keys():
            nt_absent = {}
            nt_absent['G'] = 0
            nts.update(nt_absent)
        if 'C' not in nts.keys():
            nt_absent2 = {}
            nt_absent2['C'] = 0
            nts.update(nt_absent2)         
        return nts
    #Question6: GC content method
    ##a. Add in a method that calculates and returns the GC content.
    def gc_cont(self):
        nts={}
        for nt in self.sequence:
            if nt in nts:
                nts[nt] += 1
            else:
                nts[nt] = 1
        if 'G' not in nts.keys():
            nt_absent = {}
            nt_absent['G'] = 0
            nts.update(nt_absent)
        if 'C' not in nts.keys():
            nt_absent2 = {}
            nt_absent2['C'] = 0
            nts.update(nt_absent2) 
        G = nts['G']
        C = nts['C']
        T = nts['T']
        A = nts['A']
        gc_content = (G+C)/(A+T+G+C)
        return gc_content
    def fasta_form(self):
        key = '>'+ self.gene_name + ' ' + self.species_name
        dict = {}
        value = self.sequence
        dict[key] = value
        return dict


#Question3: Write some some lines of code, outside your class that:
##a. uses the object sequence attribute to retrieve and print the sequence.
##b. uses the object name attribute to retrieve and print the name.
##c. uses the object organism attribute to retrieve and print the organism.
dna_seq_obj_1 = DNAseq('ACTGATCGTTACGTACGAT', 'ABC1', 'Drosophila melanogaster')
dna_seq_obj_2 = DNAseq('ATATATTATTATATTATA', 'COX1', 'Homo sapiens')
for d in [dna_seq_obj_1, dna_seq_obj_2]:
    print('name:', d.gene_name, '\t', 'seq:', d.sequence, '\t', 'organism:', d.species_name)
##Question4b. Write some some lines of code, outside your class (in your main program) that gets and prints the sequence length using your new method.  
    print('seq length:' + str(d.len_seq()))
##Question5b. Write some some lines of code, outside your class (in your main program) that gets and prints the sequence nucleotide compositio using your new method.
    print(f'nucleotide composition: {d.nt_comp()}')
##Question6b. Write some some lines of code, outside your class (in your main program) that gets and prints the sequence GC content using your new method.
    print(f'% GC content: {d.gc_cont():.1%}')
##Question7b. Write some some lines of code, outside your class (in your main program) that gets and prints the sequence in FASTA format using your new method.
    print(f'FASTA format: {d.fasta_form()}')