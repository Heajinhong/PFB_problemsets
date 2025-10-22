#!/usr/bin/env python3
import re
seq = ''
dict = {}
with open("Python_08_test.fasta.txt", "r") as seq_read:
    for line in seq_read:
        line = line.rstrip()
        if line.startswith('>'):
            new_line = re.sub(r"(>.\S+)(\s.+)", r"\1", line)
            dict[new_line] = ''
        else:
            dict[new_line] += line
    #print(dict)
    for key,value in dict.items():
        #print(key,value)
        for i in range(3):
            seq = value[i:]
            codons = re.findall(r"(.{1,3})", seq) 
            print(f'{key}-frame-{i+1}-codons\n{' '.join(codons)}')
            rev = ''.join(codons)
            rev = rev[::-1]
            rev = rev.replace('A', 't').replace('T','a').replace('C','g').replace('G','c').upper()
            rev_codons = re.findall(r"(.{1,3})", rev) 
            print(f'{key}-rev-comp-{i+1}-codons\n{' '.join(rev_codons)}')
    print("hired.")
                # nt = nt.replace('A', 't')
                # nt = nt.replace('T', 'a')
                # nt = nt.replace('C', 'g')
                # nt = nt.replace('G', 'c')
                # nt = nt[::-1]
                # nt = nt.upper()
            #print(f'{key}-frame-{i+1}-codons\n{' '.join(codons)}\n{key}-rev-comp-{i+1}-codons\n{nt}')    
        # dict[key] = codons   
        
    
