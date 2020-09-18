#!/usr/bin/env python3
"""
Calculate the mass of an input protein.
Usage: ./prtm.py [input file]
"""

import sys
from tools import check_input, aa_mass

def calculate_weight(protein_string, aa_weights):
    """Calculate total weight of a protein sequence."""
    total_weight = 0
    for p in protein_string:
        total_weight += aa_weights[p]
    return format(total_weight, ".3f")

def main():
    """Calculate mass of input protein sequence."""
    check_input(sys.argv[0])
    input_protein = ""
    with open(sys.argv[1]) as infile:
        for line in infile:
            input_protein += line.strip()

    print(calculate_weight(input_protein, aa_mass))

if __name__ == "__main__":
    main()
