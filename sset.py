#!/usr/bin/env python3

import sys
from tools import check_input
from mmch import perm

def count_subsets(num):
    """
    Returns the total number of subsets in the set {1, 2, ..., num}
    modulo 1,000,000.
    """
    return (2 ** num) % 1000000

def main():
    check_input(sys.argv[0])
    with open(sys.argv[1]) as infile:
        in_num = int(infile.readline().strip())
        print(count_subsets(in_num))

if __name__ == "__main__":
    main()