#!/usr/bin/env python3
"""
Completing a tree
Usage: ./tree.py [input file]
"""

import sys
from tools import check_input

def complete_tree(n, adj_list):
    """
    Calculate minimum number of edges required to convert a graph (represented
    as an adjacency list) into a tree.
    """
    edges = len(adj_list)
    return n - edges - 1

def main():
    """Produce a tree."""
    check_input(sys.argv[0])
    with open(sys.argv[1]) as infile:
        adj_list = []
        nodes = int(infile.readline().strip())
        for line in infile:
            adj_list.append([int(i) for i in line.split()])

    print(complete_tree(nodes, adj_list))

if __name__ == "__main__":
    main()
