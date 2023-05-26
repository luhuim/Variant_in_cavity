#!/bin/bash

#Adding header into output file
head -n 1 merge_data_part_00_output.tsv > variant_cavity.tsv
#Adding rest data into output file
tail -n +2 -q merge_data_part_*_output.tsv >> variant_cavity.tsv

