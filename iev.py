#!/usr/bin/env python3
"""
Calculating expected offspring
Usage: ./iev.py [input file]
"""

import sys
from tools import check_input

def calculate_average(pop_list, expected):
    """
    Calculate the expected number of offspring displaying the dominant
    phenotype in the next generation.
    """
    resulting_dom = 0
    for i, geno in enumerate(pop_list):
        resulting_dom += 2 * int(geno) * expected[i + 1]

    return resulting_dom

def main():
    """Calculate the size of the next population."""
    check_input(sys.argv[0])
    expected_offspring = {1: 1, 2: 1, 3: 1, 4: 0.75, 5: 0.5, 6: 0}
    with open(sys.argv[1]) as infile:
        data = infile.readline().strip().split(" ")
        print(calculate_average(data, expected_offspring))

if __name__ == "__main__":
    main()
