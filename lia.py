#!/usr/bin/env python3
"""
Independent alleles
Usage: ./lia.py [input file]
"""

import sys
from tools import check_input
from math import factorial

def binom(n, k, p):
    """Calculate the probability of observing n successes out of k where p 
    is the probability of getting a success."""

    return factorial(k)/(factorial(n)*factorial(k-n)) * (p**n) * ((1-p)**(k-n))

def calculate_lia(k, n):
    """
    Return the probability that at least n AaBb organisms will belong
    to the kth generation. Assume independent assortment of the genes (i.e.
    they are not linked).
    """
    # Size of kth generation
    gen_size = 2**k

    prob = 0
    for num in range(n):
        prob += binom(num, gen_size, 0.25)

    return round(1-prob, 3)

def main():
    """Calculate and print probability."""
    check_input(sys.argv[0])

    with open(sys.argv[1]) as infile:
        args = [int(i) for i in infile.readline().strip().split()]
        print(calculate_lia(args[0], args[1]))

if __name__ == "__main__":
    main()


