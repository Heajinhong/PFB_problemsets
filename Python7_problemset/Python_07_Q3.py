#!/usr/bin/env python3
import re
fasta_read = open("Python_07.fasta","r")
fasta = fasta_read.read()
found_header = re.findall(r'>.+',fasta)
print(found_header)