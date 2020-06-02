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
    rev_seq = rev_comp(seq)
    total_length = len(seq)

    rnas = []

    for i in range(3):
        remaining = total_length - i
        orf_length = remaining - (remaining % 3)
        orfs.append(rna(seq[i:i+orf_length]))  # Sense strand
        orfs.append(rna(rev_seq[i:i+orf_length]))  # Antisense strand

    return rnas

def to_mrna(seq):
    """
    Given an RNA sequence, return the mRNA representing the ORF, from start to stop codons.
    """
    start = "AUG"
    stop = ["UAG", "UGA", "UAA"]

    final_mrna = ""
    is_orf = False
    i = 0

    while i < (len(seq)-2) and not is_orf:
        if seq[i:i+3] == start:
            is_orf = True
            final_mrna += seq[i:i+3]
        i += 3

    while i < (len(seq)-2) and is_orf:
        if seq[i:i+3] in stop:
            is_orf = False
        else:
            final_mrna += seq[i:i+3]
            i += 3

    return final_mrna


test_seq = "AGCCATGTAGCTAACTCAGGTTACATGGGGATGACCCCGCGACTTGGATTAGAGTCTCTTTTGGAATAAGCCTGAATGATCCGAGTAGCATCTCAG"
# print(find_all_rnas(test_seq))
# t = "AUGCGA"
# print(to_mrna(t))

def main():
    infile = sys.argv[1]
    for _, seq in read_fasta(infile):
        inseq = seq
        print(inseq)



if __name__ == "__main__":
    main()





