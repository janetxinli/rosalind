#!/usr/bin/env python3
"""
Open reading frames.
Usage: python3 orf.py <input> > output.txt
"""

import sys
from read_fasta import read_fasta
from revc import rev_comp
from rna import rna
from prot import translate

def find_all_rnas(seq):
    """
    Given a sequence, return rna strings from all 6 reading frames.
    """

    # Compute reverse complement of sequence
    rev_seq = rev_comp(seq)

    # Calculate total length of sequence
    total_length = len(seq)

    rnas = []

    # Iterate over each codon frame
    for i in range(3):
        remaining = total_length - i
        orf_length = remaining - (remaining % 3)

        # Keep track of possible RNA strings
        rnas.append(rna(seq[i:i+orf_length]))  # Sense strand
        rnas.append(rna(rev_seq[i:i+orf_length]))  # Antisense strand

    return rnas

def to_mrna(seq):
    """
    Given an RNA sequence, return the mRNA representing the ORF, from start to stop codons.
    """
    start_codon = "AUG"
    stop = ["UAG", "UGA", "UAA"]

    # Keep track of all possible start positions
    start_positions = []
    final_mrnas = []
    i = 0

    # Find all start positions preceding a stop codon
    while i < len(seq) - 2:
        if seq[i:i+3] == start_codon:  # At start codon
            start_positions.append(i)
        i += 3

    # Keep track of all possible ORFs
    for pos in start_positions:
        mrna = ""
        i = pos
        is_orf = True
        while i < (len(seq)-2) and is_orf:
            if seq[i:i+3] in stop:  # Stop codon reached
                is_orf = False
                final_mrnas.append(mrna)
            else:  # Append codon to mRNA sequence
                mrna += seq[i:i+3]
                i += 3

    return final_mrnas

def main():
    infile = sys.argv[1]

    # Load input sequence
    for _, seq in read_fasta(infile):
        inseq = seq

    # Translate all reading frames into RNA
    rna_reading_frames = find_all_rnas(inseq)

    orfs = []

    # Find all ORFs
    for rna in rna_reading_frames:
        orfs.extend(to_mrna(rna))

    # Create a set of unique ORFs
    unique_orfs = set(orfs)

    for orf in unique_orfs:
        peptide = translate(orf)
        if len(peptide) > 0:
            print(translate(orf), file=sys.stdout)

if __name__ == "__main__":
    main()
