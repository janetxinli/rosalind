#!/usr/bin/env python3
"""
Finding a motif in DNA
Usage: ./subs.py [input file]
"""

import sys
from tools import check_input

def substring_location(string, sub):
    """Given a string and a substring, return all locations of the substring within 
    the string as a list."""
    locations = ""
    for i in range(len(string)-len(sub)+2):
        if string[i:i+len(sub)].upper() == sub.upper():
            locations += str(i+1) + " "
    return locations.strip()

def main():
    """Find substrings."""
    check_input(sys.argv[0])
    with open(sys.argv[1]) as infile:
        lines = infile.readlines()
        print(substring_location(lines[0].strip(), lines[1].strip()))

if __name__ == "__main__":
    main()