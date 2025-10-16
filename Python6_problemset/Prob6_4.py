#!/usr/bin/env python3
with open("Python_06.fastq","r") as seq_read, open("Python_06.fastq.calc.txt","w") as seq_write:
    count = 0
    countID = 0
    total_character_count = 0
    total_nucleotide_count = 0 
    for line in seq_read:
        line = line.rstrip()
        count+=1
        if line.startswith('@HWI'):
            countID+=1
        count_characters = len(line)
        total_character_count += count_characters
        if (count+2)%4==0:
            count_nucleotides = len(line)
            total_nucleotide_count += count_nucleotides    
    print(f'Total number of lines is {count}')
    print(f'Total number of sequence IDs is {countID}')
    print(f'Total number of characters is {total_character_count}')
    print(f'Total number of nucleotides is {total_nucleotide_count}')
    average_line_length = (total_character_count/count)
    print(f'The average length of all the lines is {average_line_length}')
    average_nuc_line_length = (total_nucleotide_count/(count/4))
    print(f'The average length of the nucleotides {average_nuc_line_length}')

  


                
    
