#!/usr/bin/env python3
"""
Introduction to random strings
Usage: ./prob.py [input file]
"""

import sys
from math import log10
from tools import check_input

def find_log_probabilites(seq, prob_array):
    """Return a probability array that represents the common logarithm
    of the probability that a random string constructed with the GC-content
    found in prob_array[k] will match seq exactly."""
    log_prob = []
    for prob in prob_array:
        gc = float(prob) / 2
        at = 0.5 - gc
        cur_prob = 1
        for nuc in seq:
            if nuc in "AT":
                cur_prob *= at
            elif nuc in "GC":
                cur_prob *= gc
        log_prob.append(round(log10(cur_prob), 3))

    return log_prob

def main():
    """Calculate probabilities for input."""
    check_input(sys.argv[0])
    with open(sys.argv[1]) as infile:
        seq = infile.readline().strip()
        prob = infile.readline().strip().split(" ")

    print(" ".join([str(i) for i in find_log_probabilites(seq, prob)]))

if __name__ == "__main__":
    main()
