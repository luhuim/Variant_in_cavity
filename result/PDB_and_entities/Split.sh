#!/bin/bash
INPUT=merge_data_11_23.tsv

# Step 1: split the input file without the header line
tail -n +2 "$INPUT" | split -d -l 4000 - merge_data_part_ 

# Step 2: add the header line to each split file
for file in merge_data_part_*
do
    head -n 1 "$INPUT" >> with_header_tmp
    cat "$file" >> with_header_tmp
    mv -f with_header_tmp "$file"
done

