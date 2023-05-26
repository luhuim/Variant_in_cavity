#!/usr/bin/python3
"""
Title: Writing Parameter file
Date: 2022 October 27th
Author: Huimin Lu

Description:
    This program is to write the paramiter file in every PDB id.
    require a list of pdb id
    
    
List of function:
    
Procedure:
    1. Open the list of PDB id 

Usage: 
    type code below in the command line:
    python Writing_Parameter.py sample_1.tsv ciclop_parameters.txt
    
"""

import sys

PDB_ID=sys.argv[1]
w=open(sys.argv[2],'w')


if len(str(PDB_ID))==0:
    pass
else:
    PDB_FILE="PDB_File_Name: "+str(PDB_ID.strip())+".pdb"
    print(PDB_FILE,file=w)
    FASTA_FILE="FASTA_FILE_NAME: "+str(PDB_ID.strip())+".FASTA"
    print(FASTA_FILE,file=w)
    print("Alignment: 1 \nCons_score: NO\nRate_inf_method: EB\nEvo_model: JCamino\nE_value: 10",file=w)
    print("Blast_method: j",file=w)
    print("nr_db: /home/inf-31-2021/Research_Project/Fourth/CICLOP/dist/nr",file=w)
    print("swissprot: /home/inf-31-2021/Research_Project/Fourth/CICLOP/dist/uniprot_sprot.fasta",file=w)
    print("psiblast: /home/inf-31-2021/Research_Project/Fourth/CICLOP/dist/ncbi-blast-2.13.0+/bin/psiblast",file=w)
    print("jackhmmer: /home/inf-31-2021/Research_Project/Fourth/CICLOP/dist/hmmer-3.3.2/makeTAGS.sh\n",file=w)

