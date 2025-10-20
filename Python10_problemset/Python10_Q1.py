#!/usr/bin/env python3
#Question1 Create a function to format a string of DNA so that each line is no more than 60 nt long. Your function will:
#INPUT: a string of DNA without newlines
#OUTPUT: a string of DNA with lines no more than 60 nucleotides long
import re
def split_fx(file, width):  
    with open(file, "r") as dna: #question4 
        total_seq = ""    
        fasta_dict = {}  
        for line in dna:
            line = line.rstrip()
            if line.startswith('>'):
                # key = line.lstrip('>')
                key = re.search(r"(>.\S+)", line)
                key = key.group(1)
                fasta_dict[key] = ''
            else:
                fasta_dict[key] += line
        for keys in fasta_dict.keys():
            seq = fasta_dict[keys]
            #print(seq)
            dna = re.sub(r'\s', r"", seq) #this is for question2
            splits = re.findall(r"(.{1,"+str(width)+"})", dna) #question3
            joint = '\n'.join(splits)
            fasta_dict[keys] = joint
    return fasta_dict

# # dna = 'GATGGGATTGGGGTTTTCCCCTCCCATGTGCTCAAGACTGGCGCTAAAAGTTTTGAGCTTCTCAAAAGTCTAGAGCCACCGTCCAGGGAGCAGGTAGCTGCTGGGCTCCGGGGACACTTTGCGTTCGGGCTGGGAGCGTGCTTTCCACGACGGTGACACGCTTCCCTGGATTGGCAGCCAGACTGCCTTCCGGGTCACTGCCATGGAGGAGCCGCAGTCAGATCCTAGCGTCGAGCCCCCTCTGAGTCAGGAAACATTTTCAGACCTATGGAAACTACTTCCTGAAAACAACGTTCTGTCCCCCTTGCCGTCCCAAGCAATGGATGATTTGATGCTGTCCCCGGACGATATTGAACAATGGTTCACTGAAGACCCAGGTCCAGATGAAGCTCCCAGAATGCCAGAGGCTGCTCCCCCCGTGGCCCCTGCACCAGCAGCTCCTACACCGGCGGCCCCTGCACCAGCCCCCTCCTGGCCCCTGTCATCTTCT'
# # print(split_fx(dna))

# #Question2: Modify your function so that it will work whether the DNA string does or does not have newlines.

# # dna2 = '''GATGGGATTGGGGTTTTCCCCTCCCATGTGCTCAAGACTGGCGCTAAAAGTTTTGAGCTTCTCAAAAGTCTAGAGCCACC
# # GTCCAGGGAGCAGGTAGCTGCTGGGCTCCGGGGACACTTTGCGTTCGGGCTGGGAGCGTGCTTTCCACGACGGTGACACG
# # CTTCCCTGGATTGGCAGCCAGACTGCCTTCCGGGTCACTGCCATGGAGGAGCCGCAGTCAGATCCTAGCGTCGAGCCCCC
# # TCTGAGTCAGGAAACATTTTCAGACCTATGGAAACTACTTCCTGAAAACAACGTTCTGTCCCCCTTGCCGTCCCAAGCAA
# # TGGATGATTTGATGCTGTCCCCGGACGATATTGAACAATGGTTCACTGAAGACCCAGGTCCAGATGAAGCTCCCAGAATG
# # CCAGAGGCTGCTCCCCCCGTGGCCCCTGCACCAGCAGCTCCTACACCGGCGGCCCCTGCACCAGCCCCCTCCTGGCCCCT
# # GTCATCTTCT'''
# # print(split_fx(dna2))

# #Question3: Modify your function so that it takes two arguments, the DNA string and the max length of each line.
# # dna3 = 'GATGGGATTGGGGTTTTCCCCTCCCATGTGCTCAAGACTGGCGCTAAAAGTTTTGAGCTTCTCAAAAGTCTAGAGCCACCGTCCAGGGAGCAGGTAGCTGCTGGGCTCCGGGGACACTTTGCGTTCGGGCTGGGAGCGTGCTTTCCACGACGGTGACACGCTTCCCTGGATTGGCAGCCAGACTGCCTTCCGGGTCACTGCCATGGAGGAGCCGCAGTCAGATCCTAGCGTCGAGCCCCCTCTGAGTCAGGAAACATTTTCAGACCTATGGAAACTACTTCCTGAAAACAACGTTCTGTCCCCCTTGCCGTCCCAAGCAATGGATGATTTGATGCTGTCCCCGGACGATATTGAACAATGGTTCACTGAAGACCCAGGTCCAGATGAAGCTCCCAGAATGCCAGAGGCTGCTCCCCCCGTGGCCCCTGCACCAGCAGCTCCTACACCGGCGGCCCCTGCACCAGCCCCCTCCTGGCCCCTGTCATCTTCT'
# # width = 80
# # print(split_fx(dna3, width))

# #Question4: Modify your script so that it can take two command line arguments: FASTA file name/Max length of each line
# #The script should reformat every sequence in the file to the specified max line length. Make sure your output is in proper FASTA format.
file = "Python_10.test.fasta.txt"
width = 11
fasta_dict = split_fx(file, width)
with open('Python_10.test.output.txt','w') as seq_write:
    for key in fasta_dict.keys():
        seq_write.write(f'{key}\n{fasta_dict[key]}\n')
        print(f'{key}\n{fasta_dict[key]}\n')

