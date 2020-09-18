#!/usr/bin/env python3
"""
Finding a spliced motif
Usage: ./sseq.py [input file]
"""

import sys
from tools import check_input, read_fasta

def find_subsequence(sequence, search):
    """Return a collection of indices in sequence in which the characters of search appear
    as a subsequence."""
    indices = []
    i = 0
    j = 0
    while i < len(search):
        found = False
        curr_char = search[i]
        while j < len(sequence) and not found:
            if sequence[j] == curr_char:
                indices.append(str(j+1))
                found = True
            j += 1                
        i += 1
    return " ".join(indices)

def main():
    """Find indices of a given subsequence in a given sequence."""
    check_input(sys.argv[0])
    i = 0
    for _, seq in read_fasta(sys.argv[1]):
        if i == 0:
            sequence = seq
        elif i == 1:
            search = seq
        i += 1

    print(find_subsequence(sequence, search))

if __name__ == "__main__":
    main()