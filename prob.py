#!/usr/bin/env python3

import sys
from math import log10

def find_log_probabilites(seq, prob_array):

    log_prob = []

    for prob in prob_array:
        gc = float(prob) / 2
        at = 0.5 - gc
        cur_prob = 1

        # Calculate probability
        for nuc in seq:
            if nuc in "AT":
                cur_prob *= at
            elif nuc in "GC":
                cur_prob *= gc

        log_prob.append(round(log10(cur_prob), 3))

    return " ".join([str(i) for i in log_prob])

def test():
    probs = "0.129 0.287 0.423 0.476 0.641 0.742 0.783".split()
    print(find_log_probabilites("ACGATACAA", probs))

def main():
    input = sys.stdin.readlines()

    seq = input[0].strip()
    probabilities = input[1].strip().split()

    print(find_log_probabilites(seq, probabilities))

if __name__ == "__main__":
    main()
