#!/usr/bin/env python3
"""
Given a positive integer n <= 7, return the total number
of permutations of length n, followed by a list of all such permutations.
"""

import sys

def factorial(num):
    """
    Calculate num factorial.
    """
    if num == 0:
        return 1
    elif num > 0:
        return num * factorial(num-1)

def perm(num):
    """
    Run helper function to print permutations of number.
    """
    # Create a list of numbers up to and including num
    numlist = []
    for n in range(1, num+1):
        numlist.append(str(n))

    print(factorial(num), file=sys.stdout)
    # Run permHelper function on numlist
    permHelper(numlist, 0, len(numlist)-1)

def permHelper(numlist, first, last):
    """
    Print all possible permutations of characters in numlist
    """
    # Define base case
    if last > first:

        for i in range(first, last+1):

            # Swap first and ith character in numlist
            numlist[first], numlist[i] = numlist[i], numlist[first]

            # Recursively call permHelper
            permHelper(numlist, first+1, last)

            # Swap first and ith character back
            numlist[first], numlist[i] = numlist[i], numlist[first]

    if last == first:
        print(" ".join(numlist), file=sys.stdout)

# perm(3)

if __name__ == "__main__":
    invalue = int(sys.stdin.readline().strip())
    perm(invalue)




