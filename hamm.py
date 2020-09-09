#!/usr/bin/env python3
"""
Counting point mutations
Usage: ./hamm.py [input file]
"""

import sys

def hamming_distance(s, t):
    """Calculate hamming distance between strings of equal length s and t."""
    if len(s) != len(t):
        raise TypeError("Two input strings must be of same length.")
    hamm = 0
    for i, char in enumerate(s):
        if t[i].upper() != char.upper():
            hamm += 1    
    return hamm

def main():
    """Calculate hamming distance for input file."""
    if len(sys.argv) != 2:
        print("Usage: %s [input file]" % sys.argv[0])
        sys.exit(1)
    with open(sys.argv[1]) as infile:
        string_1 = infile.readline().strip()
        string_2 = infile.readline().strip()
        print(hamming_distance(string_1, string_2))

if __name__ == "__main__":
    main()