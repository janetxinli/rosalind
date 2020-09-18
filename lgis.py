#!/usr/bin/env python3
"""
Longest increasing subsequence
Usage: ./lgis.py [input file]
"""

import sys
from tools import check_input

def longest_subsequence(sequence):
    """Return the longest increasing and longest decreasing subsequences in sequence."""
    longest_increasing = []
    longest_decreasing = []
    for num in sequence:
        longest_increasing.append([num])
        longest_decreasing.append([num])
    i = 1
    while i < len(sequence):
        j = i - 1
        while j >= 0:
            # Find longest increasing
            if sequence[j] < sequence[i] and len(longest_increasing[j]) >= len(longest_increasing[i]):
                longest_increasing[i] = longest_increasing[j] + [sequence[i]]
            # Find longest decreasing
            if sequence[j] > sequence[i] and len(longest_decreasing[j]) >= len(longest_decreasing[i]):
                longest_decreasing[i] = longest_decreasing[j] + [sequence[i]]
            j -= 1
        i += 1

    increasing = [str(i) for i in max(longest_increasing, key=lambda x: len(x))]
    decreasing = [str(i) for i in max(longest_decreasing, key=lambda x: len(x))]

    return "%s\n%s" % (" ".join(increasing), " ".join(decreasing))

def main():
    """Read input file and print longest increasing and decreasing subsequences."""
    check_input(sys.argv[0])   
    with open(sys.argv[1]) as infile:
        in_seq = infile.readlines()[1].strip().split()
        print(longest_subsequence([int(i) for i in in_seq]))

if __name__ == "__main__":
    main()