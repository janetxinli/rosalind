#!/usr/bin/env python3
"""
Locating restriction sites
Usage: ./revp.py [input file]
"""

import sys
from tools import read_fasta, check_input
from revc import rev_comp

def find_revp(in_string):
    """
    Takes as input a DNA string and yields the position (1-based) and length of every reverse palindrome
    contained in the string between 4-12 bp long.
    """
    for length in range(4, 13):
        for i in range(len(in_string) - length + 1):
            if in_string[i:i+length] == rev_comp(in_string[i:i+length]):
                yield(i+1, length)

def main():
    """Find reverse palindromes in input."""
    check_input(sys.argv[0])
    for _, seq in read_fasta(sys.argv[1]):
        for pair in find_revp(seq):
            print(*pair, sep=" ")

if __name__ == "__main__":
    main()
