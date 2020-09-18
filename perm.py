#!/usr/bin/env python3
"""
Enumerating gene orders
Usage: ./perm.py [input file]
"""

import sys
from tools import check_input

def factorial(num):
    """Calculate the factorial of num."""
    if num == 0:
        return 1
    elif num > 0:
        return num * factorial(num-1)

def perm(num):
    """Run helper function to print permutations of number."""
    # Create a list of numbers up to and including num
    numlist = []
    for n in range(1, num+1):
        numlist.append(str(n))

    print(factorial(num))
    permHelper(numlist, 0, len(numlist)-1)

def permHelper(numlist, first, last):
    """
    Print all possible permutations of characters in numlist
    """
    # Base case
    if last > first:
        for i in range(first, last+1):
            # Swap first and ith character in numlist
            numlist[first], numlist[i] = numlist[i], numlist[first]
            # Recursively call permHelper
            permHelper(numlist, first+1, last)
            # Swap first and ith character back
            numlist[first], numlist[i] = numlist[i], numlist[first]

    if last == first:
        print(" ".join(numlist))

def main():
    """Print number of permutations and all possible permutations for input number."""
    check_input(sys.argv[0])
    with open(sys.argv[1]) as infile:
        invalue = int(infile.readline().strip())
    perm(invalue)

if __name__ == "__main__":
    main()




