#!/usr/bin/env python3

import sys
import argparse
from perm import factorial, permHelper

def get_signs(end, current=1, num_list=[]):
    """Returns all possible enumerations of num (both positive and negative)."""
    if current > end:
        ALL.append(num_list.copy())
        return
    nums = [current, -current]
    for num in nums:
        num_list.append(str(num))
        get_signs(end, current + 1, num_list)
        num_list.pop()

def get_args():
    parser = argparse.ArgumentParser(description="Enumerating Oriented Gene Orderings")
    parser.add_argument("input",
                        type=argparse.FileType("r"),
                        help="A positive integer less than or equal to 6")
    return parser.parse_args()

if __name__ == "__main__":
    ALL = []
    args = get_args()
    num = int(args.input.readline().strip())
    if num > 6:
        raise TypeError("Input integer must be less than or equal to 6")
        sys.exit(1)
    print((2**num) * factorial(num), file=sys.stdout)
    get_signs(num)
    for l in ALL:
        permHelper(l, 0, len(l)-1)
