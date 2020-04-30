#!/usr/bin/env python3
"""
Given a DNA string, return the position (1-based) and length of every reverse palindrome in the string.
"""

import sys
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

    # Assign DNA string from input fasta file to a single variable
    dna_string = ""

    # Iterate over lines in input file.
    for line in sys.stdin:
        if line[0] == ">":  # Header string; skip
            continue
        else:  # Append all lines containing DNA string to dna_string
            dna_string += line.strip()

    # Find reverse palindromes in input DNA string and print to stdout.
    for pair in find_revp(dna_string):
        print(*pair, sep=" ")

    # testcase = "TCAATGCATGCGGGTCTATATGCAT"
    # for pair in find_revp(testcase):
    #     print(*pair, sep=" ")

if __name__ == "__main__":
    main()
