#!/usr/bin/env python3
"""
Independent alleles
"""

import sys
from math import factorial

def binom(n, k, p):
    """Calculate the probability of observing n successes out of k where p is the probability of
    getting a success."""

    return factorial(k)/(factorial(n)*factorial(k-n)) * (p**n) * ((1-p)**(k-n))

def calculate_lia(k, n):
    """
    Return the probability that at least n AaBb organisms will belong
    to the kth generation. Assume independent assortment of the genes (i.e.
    they are not linked).
    """
    # Calculate size of kth generation
    gen_size = 2**k

    # Calculate probability of getting n-1 individuals
    prob = 0

    for num in range(n):
        prob += binom(num, gen_size, 0.25)

    return round(1-prob, 3)

if __name__ == "__main__":
    # print(calculate_lia(2, 1))

    # Read input values from stdin
    info = sys.stdin.read().strip()
    args = info.split()

    print(calculate_lia(int(args[0]), int(args[1])), file=sys.stdout)


