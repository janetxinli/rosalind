#!/usr/bin/env python3
"""
Complementing a strand of DNA
Usage: ./revc.py [input file]
"""

import sys
from tools import check_input

def rev_comp(dna_strand):
    """Return the reverse complement of a strand of DNA."""
    new_strand = ''
    for nuc in dna_strand:
        if nuc == 'A':
            new_strand = 'T' + new_strand
        elif nuc == 'T':
            new_strand = 'A'+ new_strand
        elif nuc == 'G':
            new_strand = 'C' + new_strand
        elif nuc == 'C':
            new_strand = 'G' + new_strand
    return new_strand

def main():
    """Reverse complement input DNA sequence."""
    check_input(sys.argv[0])
    with open(sys.argv[1]) as infile:
        sequence = infile.readline().strip()
    print(rev_comp(sequence))

if __name__ == "__main__":
    main()
