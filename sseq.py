#!/usr/bin/env python3

import argparse
from read_fasta import read_fasta

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


def get_args():
    parser = argparse.ArgumentParser(description="Find the indices of a spliced motif")
    parser.add_argument("input",
                        type=str,
                        help="Input file")
    return parser.parse_args()

def main():
    args = get_args()
    i = 0
    for _, seq in read_fasta(args.input):
        if i == 0:
            sequence = seq
        elif i == 1:
            search = seq
        i += 1
    
    print(find_subsequence(sequence, search))


if __name__ == "__main__":
    main()