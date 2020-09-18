#!/usr/bin/env python3
"""
Translating RNA into protein
Usage: ./prot.py [input file]
"""

import sys
from tools import genetic_code, check_input

def translate(rna_string):
    """Translate an RNA string into a protein string."""
    if len(rna_string) % 3 != 0:
        raise ValueError("Input RNA string must be divisible by 3.")
    peptide = ""
    codon_list = [rna_string[i:3+i].upper() for i in range (0, len(rna_string), 3)]
    for codon in codon_list:
        if codon == "UAA":
            continue
        elif codon == "UAG":
            continue
        elif codon == "UGA":
            continue
        else:
            peptide += genetic_code[codon]
    return peptide

def main():
    """Translate input string."""
    check_input(sys.argv[0])
    input_string = ""
    with open(sys.argv[1]) as infile:
        for line in infile:
            input_string += line.strip()
    print(translate(input_string))

if __name__ == "__main__":
    main()