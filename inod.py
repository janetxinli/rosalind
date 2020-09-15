#!/usr/bin/env python3
"""
Counting phylogenetic ancestors
Usage: ./inod.py [input file]
"""

import sys
from tools import check_input

def count_ancestors(leaves):
    """Given the number of leaves in an unrooted binary tree, return
    the number of internal nodes in that tree."""
    
    return leaves - 2

def main():
    check_input(sys.argv[0])
    with open(sys.argv[1]) as infile:
        print(count_ancestors(int(infile.readline().strip())))

if __name__ == "__main__":
    main()