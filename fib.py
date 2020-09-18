#!/usr/bin/env python3
"""
Rabbits and recurrence relations
Usage: ./fib.py [input file]
"""

import sys
from tools import check_input

def fib_rabbits(months, litter):
    """
    Calculate the number of rabbit pairs present after months if each reproductive
    pair produces a litter of size litter.
    """
    if months == 0:
        return 0
    elif months == 1:
        return 1
    # Every pair reproductive the month before will still be reproductive
    reproductive = fib_rabbits(months - 1, litter)
    # Every pair from two months ago will produce a litter
    young = litter * fib_rabbits(months - 2, litter)
    
    return reproductive + young

def main():
    """Count rabbits."""
    check_input(sys.argv[0])
    with open(sys.argv[1]) as infile:
        inputs = infile.readline().strip().split(" ")
        print(fib_rabbits(int(inputs[0]), int(inputs[1])))

if __name__ == "__main__":
    main()