#!/usr/bin/env python3
"""
Overlap Graphs
Usage: ./grph.py [input file]
"""

import sys
from tools import read_fasta

def prefix(dna_string):
    """Returns the 3 nucleotide long prefix of dna_string."""
    return dna_string[:3]

def suffix(dna_string):
    """Returns the 3 nucleotide long suffix of dna_string."""
    return dna_string[-3:]

def main():
    """Loads all sequences from the input fasta file."""
    if len(sys.argv) != 2:
        print("Usage: %s [input file]" % sys.argv[0])
        sys.exit(1)
    sequences = {}
    overlaps = Graph()

    for header, seq in read_fasta(sys.argv[1]):
        sequences[header] = seq

    for header_1 in sequences:
        for header_2 in sequences:
            if sequences[header_1] != sequences[header_2]:  # Only compare different seqs
                if suffix(sequences[header_1]) == prefix(sequences[header_2]):
                    print(header_1, header_2, file=sys.stdout)

if __name__ == "__main__":
    main()
