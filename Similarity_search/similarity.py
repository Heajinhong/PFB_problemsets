#!/usr/bin/env python3
import sys

field_names = ['qseqid','sseqid','percid','alen','mismat','gaps','q_start','q_end','s_start','s_end','evalue','bits']
hits_list = []
for hit_file in sys.argv[1:]:
    with open(hit_file,"r") as seq_read:
        for line in seq_read:
            line = line.rstrip()
            if line.startswith('#'):
                continue
            this_data = dict(zip(field_names, line.split('\t')))
            #print(this_data)cd
            this_data['file'] = hit_file()
            hits_list.append(this_data)
            break
#print(hits_list)
for hit in hits_list:
    print('\t'.join([hit[x] for x in ('file','percid','alen','evalue')]))

