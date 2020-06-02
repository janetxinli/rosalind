#!/usr/bin/env python3
"""
Write all permutations from a given alphabet and length. Print to stdout.
"""

import sys

def lexi(alpha, letters, final=None):

    if letters > 0:
        if final == None:
            final = []

        for char in alpha:
            final.append(char)
            lexi(alpha, letters-1, final)
            final.pop()

    if letters == 0:
        print("".join(final), file=sys.stdout)

if __name__ == "__main__":
    # alpha = ["A", "C", "G", "T"]
    # lexi(alpha, 2)

    # Load stdin
    input = sys.stdin

    # Load first line of input as alphabet
    alpha = input.readline().strip().split(" ")

    # Load second line of input as number of letters
    letters = int(input.readline().strip())

    lexi(alpha, letters)