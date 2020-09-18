#!/usr/bin/env python3
"""
Transcribing DNA into RNA
Usage: ./rna.py [input file]
"""

import sys
from tools import check_input

def rna(dna_string):
    """Transcribe DNA sequence to RNA."""
    trans_string = ''
    for nuc in dna_string:
        if nuc == 'T':
            trans_string += 'U'
        else:
            trans_string += nuc
    return trans_string

def main():
    check_input(sys.argv[0])
    seq = ""
    with open(sys.argv[1]) as infile:
        for line in infile:
            seq += line.strip()
    
    print(rna(seq))

if __name__ == "__main__":
    main()