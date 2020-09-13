#!/usr/bin/env python3

import sys

def complete_tree(n, adj_list):
    edges = len(adj_list)

    return n - edges - 1

def main():
    nodes = int(sys.stdin.readline().strip())
    adj_list = []

    line = sys.stdin.readline().strip()
    while line:
        adj_list.append([int(i) for i in line.split()])
        line = sys.stdin.readline().strip()

    print(complete_tree(nodes, adj_list))

if __name__ == "__main__":
    main()
