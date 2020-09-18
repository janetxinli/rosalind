#!/usr/bin/env python3
"""
Mortal fibonacci rabbits
Usage: ./fibd.py [input file]
"""

import sys
from tools import check_input

def mortal_fib_rabbits(n, m):
    """
    Count the total number of pairs of rabbits that will remain after n months
    if all rabbits live for m months.
    """
    # Create a list to hold number of rabbits of each age
    ages = [0] * m
    ages[1] = 1
    month = 3

    if n < 3:
        return 1
    else:
        while month <= n:
            reproductive = 0
            for i in range(1, m):
                reproductive += ages[i]
            ages[m-1] = 0
            for i in range(m-1, 0, -1):
                ages[i] += ages[i-1]
                ages[i-1] = 0
            ages[0] += reproductive
            month += 1

    return sum(ages)

def main():
    """Count mortal rabbits."""
    check_input(sys.argv[0])
    with open(sys.argv[1]) as infile:
        inputs = infile.readline().strip().split(" ")
        print(mortal_fib_rabbits(int(inputs[0]), int(inputs[1])))

if __name__ == "__main__":
    main()
