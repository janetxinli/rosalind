#!/usr/bin/env python3

import sys
from math import factorial

def partial_permutations(n, k):
    """Calculates the number of partial permutations from choosing k objects from n."""

    return int((factorial(n) / factorial(n - k)) % 1000000)

def main():
    input = sys.stdin.readline().strip().split()

    n = int(input[0])
    k = int(input[1])

    print(partial_permutations(n, k))

if __name__ == "__main__":
    main()
