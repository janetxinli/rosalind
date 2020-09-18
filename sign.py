#!/usr/bin/env python3
"""
Enumerating oriented gene orderings
Usage: ./sign.py [input file]
"""

import sys
import argparse
from tools import check_input, read_fasta
from perm import factorial, permHelper

def main():
    check_input(sys.argv[0])
    enum_list = []
    with open(sys.argv[1]) as infile:
        num = int(infile.readline().strip())
    print((2**num) * factorial(num))
    get_signs(num, enum_list)
    for l in enum_list:
        permHelper(l, 0, len(l)-1)

def get_signs(end, total_list, current=1, num_list=[]):
    """Returns all possible enumerations of num (both positive and negative)."""
    if current > end:
        total_list.append(num_list.copy())
        return
    nums = [current, -current]
    for num in nums:
        num_list.append(str(num))
        get_signs(end, total_list, current + 1, num_list)
        num_list.pop()

if __name__ == "__main__":
    main()
