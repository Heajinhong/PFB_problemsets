#!/usr/bin/env python3
count = {}
with open("Python_06.seq.txt","r") as seq_read:
    for line in seq_read:
        line = line.rstrip()
        seqName,sequence = line.split('\t')
        nts = {}
        for nt in sequence:
            if nt in nts:
                nts[nt] += 1
            else:
                nts[nt] = 1
        count[seqName] = nts
print(count)
for seqName in count:
    nts = count[seqName]
    GC_content = f"{(nts['G'] + nts['C'])/(nts['G']+nts['A']+nts['T']+nts['C']):.1%}"
    print(f'{seqName} has {GC_content} GC')

            
