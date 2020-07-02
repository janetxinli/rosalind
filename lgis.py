#!/usr/bin/env python3

import sys

def longest_subsequence(sequence):
    """Returns the longest increasing and longest decreasing subsequences in sequence."""

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

    return "{i}\n{d}".format(i=" ".join(increasing), d=" ".join(decreasing))

if __name__ == "__main__":
    input = sys.stdin.readlines()
    in_seq = input[1].strip().split()

    for i, item in enumerate(in_seq):
        in_seq[i] = int(item)

    print(longest_subsequence(in_seq))