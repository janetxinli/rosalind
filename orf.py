#!/usr/bin/env python3
"""
Open reading frames.
Usage: ./orf.py [input file]
"""

import sys
from tools import read_fasta, check_input
from revc import rev_comp
from rna import rna
from prot import translate

def find_all_rnas(seq):
    """Given a sequence, return rna strings from all 6 reading frames."""
    rev_seq = rev_comp(seq)
    total_length = len(seq)
    rnas = []
    for i in range(3):
        remaining = total_length - i
        orf_length = remaining - (remaining % 3)
        rnas.append(rna(seq[i:i+orf_length]))  # Sense strand
        rnas.append(rna(rev_seq[i:i+orf_length]))  # Antisense strand

    return rnas

def to_mrna(seq):
    """
    Given an RNA sequence, return the mRNA representing the ORF, from start 
    to stop codons.
    """
    start_codon = "AUG"
    stop = ["UAG", "UGA", "UAA"]
    start_positions = []
    final_mrnas = []
    i = 0
    while i < len(seq) - 2:
        if seq[i:i+3] == start_codon:  # At start codon
            start_positions.append(i)
        i += 3

    for pos in start_positions:
        mrna = ""
        i = pos
        is_orf = True
        while i < (len(seq)-2) and is_orf:
            if seq[i:i+3] in stop:  # Stop codon reached
                is_orf = False
                final_mrnas.append(mrna)
            else:
                mrna += seq[i:i+3]
                i += 3

    return final_mrnas

def main():
    """Find all candidate protein strings."""
    check_input(sys.argv[0])
    for _, seq in read_fasta(sys.argv[1]):
        inseq = seq

    rna_reading_frames = find_all_rnas(inseq)
    orfs = []
    for rna in rna_reading_frames:
        orfs.extend(to_mrna(rna))
    
    unique_orfs = set(orfs)
    for orf in unique_orfs:
        peptide = translate(orf)
        if len(peptide) > 0:
            print(translate(orf), file=sys.stdout)

if __name__ == "__main__":
    main()
