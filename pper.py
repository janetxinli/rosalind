#!/usr/bin/env python3
"""
Partial permutations
Usage: ./pper.py [input file]
"""

import sys
from math import factorial
from tools import check_input

def partial_permutations(n, k):
    """Calculates the number of partial permutations from choosing k objects from n."""
    return int((factorial(n) / factorial(n - k)) % 1000000)

def main():
    """Count total partial permutations for input."""
    check_input(sys.argv[0])
    with open(sys.argv[1]) as infile:
        n = int(infile.readline().strip())
        k = int(infile.readline().strip())

    print(partial_permutations(n, k))

if __name__ == "__main__":
    main()
