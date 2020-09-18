#!/usr/bin/env python3
"""
Inferring mRNA from Protein
Usage: ./mrna.py [input file]
"""

import sys
from tools import check_input

def possible_mrnas(seq, codon_table):
    """
    Given an amino acid sequence, return the total number of RNA strings from which the
    protein could have been translated, modulo 1,000,000.
    """
    # Set total to 1 for methionine
    total = 1
    i = 0
    while i < len(seq):
        total = total * codon_table[seq[i]]
        i += 1

    return (total * 3) % 1000000

def main():
    """Calculate total number of different RNA strings for the input."""
    check_input(sys.argv[0])
    
    # Amino acids and # of codons that code for them
    NUM_CODONS = {"I": 3, "L": 6, "V": 4, "F": 2, "M": 1, "C": 2, "A": 4,
              "G": 4, "P": 4, "T": 4, "S": 6, "Y": 2, "W": 1, "Q": 2,
              "N": 2, "H": 2, "E": 2, "D": 2, "K": 2, "R": 6, "Stop": 3}
    
    with open(sys.argv[1]) as infile:
        aa_seq = infile.readline().strip()

    print(possible_mrnas(aa_seq, NUM_CODONS))

if __name__ == "__main__":
    main()

