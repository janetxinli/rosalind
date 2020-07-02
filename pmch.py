#!/usr/bin/env python3

import sys
from read_fasta import read_fasta
from math import factorial

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
    input = sys.argv[1]

    for _, seq in read_fasta(input):
        print(str(perfect_matchings(seq)))

if __name__ == "__main__":
    main()
