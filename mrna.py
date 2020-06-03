#!/usr/bin/env python3

import sys

# Create a dictionary holding amino acids and number of codons that code for it
num_codons = {"I": 3, "L": 6, "V": 4, "F": 2, "M": 1, "C": 2, "A": 4,
              "G": 4, "P": 4, "T": 4, "S": 6, "Y": 2, "W": 1, "Q": 2,
              "N": 2, "H": 2, "E": 2, "D": 2, "K": 2, "R": 6, "Stop": 3}

def possible_mrnas(seq):
    """
    Given an amino acid sequence, return the ttal number of RNA strings from which the
    protein could have been translated, modulo 1,000,000.
    """
    # Set total to 1 for methionine
    total = 1
    i = 0

    # For each amino acid, multiply total by possible codons
    while i < len(seq):
        total = total * num_codons[seq[i]]
        i += 1

    # Return total possible sequences mod 1,000,000
    return (total * 3) % 1000000

def main():
    # Read amino acid sequence from stdin
    aa_seq = sys.stdin.readline().strip()
    # Print possible sequences to stdout
    print(possible_mrnas(aa_seq), file=sys.stdout)

if __name__ == "__main__":
    main()

