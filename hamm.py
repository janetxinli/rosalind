#!/usr/bin/env python3
"""
Given two strings of equal length, determine the Hamming distance (number of corresponding characters that differ
between the two). Return the Hamming distance as an integer.
"""

def hamming_distance(s, t):
    if len(s) != len(t):
        raise RuntimeError("Two input strings must be of same length.")

    hamm = 0

    for i, char in enumerate(s):
        if t[i].upper() == char.upper():
            continue
        else:
            hamm += 1

    return hamm