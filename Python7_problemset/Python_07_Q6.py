#!/usr/bin/env python3
import re
with open("Python_07_ApoI.fasta","r") as seq_read:
    seq_read = seq_read.read()
    for ApoI in re.findall(r"[AG]AATT[CT]", seq_read):
        print(ApoI)

