#!/usr/bin/env python3
import re
fasta_read = open("Python_07.fasta","r")
fasta = fasta_read.read()
for (id,desc) in re.findall(r"(>.\S+)\s(.+)",fasta):
    print("id:", id)
    print("desc:", desc)