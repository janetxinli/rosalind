#!/usr/bin/env python3
"""
Enumerating k-mers lexicographically
Usage: ./lexf.py [input file]
"""

import sys
from tools import check_input

def lexi(alpha, k, final=None):
    """Given an alphabet and number of letters k, print all kmers
    of the alphabet in lexicographical order."""
    if k > 0:
        if final == None:
            final = []

        for char in alpha:
            final.append(char)
            lexi(alpha, k-1, final)
            final.pop()

    if k == 0:
        print("".join(final), file=sys.stdout)

def main():
    """Print enumerated kmers for input k and alphabet."""
    check_input(sys.argv[0])
    with open(sys.argv[1]) as infile:
        alpha = infile.readline().strip().split(" ")
        k = int(infile.readline().strip())
        lexi(alpha, k)

if __name__ == "__main__":
    main()