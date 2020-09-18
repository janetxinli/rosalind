#!/usr/bin/env python3
"""
Perfect matchings and RNA secondary structures
Usage: ./pmch.py [input file]
"""

import sys
from tools import read_fasta, check_input
from perm import factorial

def perfect_matchings(seq):
    """Returns the total possible number of perfect matchings of basepair edges
    in the bonding graph for a given sequence."""
    UA = 0
    GC = 0
    for char in seq:
        if char == "U":
            UA += 1
        elif char == "G":
            GC += 1
    return factorial(UA) * factorial(GC)

def main():
    """Count perfect matchings in input sequence."""
    check_input(sys.argv[0])
    for _, seq in read_fasta(sys.argv[1]):
        print(str(perfect_matchings(seq)))

if __name__ == "__main__":
    main()
