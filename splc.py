#!/usr/bin/env python3
"""
Given a pre-mRNA sequence and intron sequences contained within that pre-mRNA, return
the resulting translated protein string from the (spliced) mRNA.
"""

import sys
from read_fasta import read_fasta
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
    # Load sequences into a list
    with open(sys.argv[1], "r") as fh:
        seqs = []
        for _, seq in read_fasta(fh):
            transcribed = rna(seq)
            seqs.append(transcribed)

    # Splice pre-mRNA
    mrna = splice(seqs)

    # Translate mRNA
    print(translate(mrna), file=sys.stdout)


if __name__ == "__main__":
    main()