#!/usr/bin/env python3
"""
Counting DNA nucleotides
Usage: ./dna.py [input file]
"""

import sys
from tools import check_input

def n_count(dna_string):
    """Count the number of occurrences of "A", "C", "G" and "T" in dna_string."""
    a_count = 0
    c_count = 0
    g_count = 0
    t_count= 0
    for nuc in dna_string:
        if nuc.upper() == 'A':
            a_count += 1
        elif nuc.upper() == 'C':
            c_count += 1
        elif nuc.upper() == 'G':
            g_count += 1
        elif nuc.upper() == 'T':
            t_count += 1
        else:
            continue
    print(a_count, c_count, g_count, t_count)

def main():
    """Count input nucleotides."""
    check_input(sys.argv[0])
    with open(sys.argv[1]) as infile:
        seq = infile.readline().strip()
        n_count(seq)
    