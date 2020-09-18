#!/usr/bin/env python3
"""
RNA splicing
Usage: ./splc.py [input file]
"""

import sys
from tools import read_fasta, check_input
from rna import rna
from prot import translate

def splice(seq_list):
    """
    Given a list of sequences where 0 is the pre-mRNA and the remaining are introns,
    return a sequence string with the introns spliced out.
    """
    mrna = seq_list.pop(0)
    for intron in seq_list:
        mrna = mrna.replace(intron, "")

    return mrna

def main():
    """Splice and translate input DNA string."""
    check_input(sys.argv[0])
    seqs = []
    for _, seq in read_fasta(sys.argv[1]):
        transcribed = rna(seq)
        seqs.append(transcribed)

    mrna = splice(seqs)
    print(translate(mrna))

if __name__ == "__main__":
    main()