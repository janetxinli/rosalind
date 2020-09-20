#!/usr/bin/env python3

import sys
from math import factorial
from tools import check_input, read_fasta

def perm(n, r):
    """
    Calculates the number of combinations nCr, where r items are chosen
    from a set of size n.
    """
    return factorial(n) // (factorial(n-r))

def maximum_matchings(sequence):
    """
    Return the total possible number of maximum matchings of basepair
    edges in the bonding graph for the given sequence.
    """
    base_counts = {"A": 0, "U": 0, "C": 0, "G": 0}
    for base in sequence:
        base_counts[base] += 1
    max_au, min_au = max(base_counts["A"], base_counts["U"]), min(base_counts["A"], base_counts["U"])
    max_gc, min_gc = max(base_counts["C"], base_counts["G"]), min(base_counts["C"], base_counts["G"])
    au_matchings = perm(max_au, min_au)
    cg_matchings = perm(max_gc, min_gc)
    return int(au_matchings * cg_matchings)

def main():
    """Count maximum matchings for the input sequence."""
    check_input(sys.argv[0])
    for _, seq in read_fasta(sys.argv[1]): 
        print(maximum_matchings(seq))

if __name__ == "__main__":
    main()