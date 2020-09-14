#!/usr/bin/env python3
"""
Creating a distance matrix
Usage: ./pdst.py [input file]
"""

import sys
from tools import check_input
from tools import read_fasta
from hamm import hamming_distance

def create_matrix(list_of_sequences):
    """Return the distance matrix for a list of sequences."""
    num_seq = len(list_of_sequences)
    len_seq = len(list_of_sequences[0])
    matrix = [[] for i in range(num_seq)]
    for i in range(num_seq):
        first_sequence = list_of_sequences[i]
        for j in range(num_seq):
            if i != j:
                second_sequence = list_of_sequences[j]
                matrix[i].append(round((hamming_distance(first_sequence, second_sequence)/len_seq), 4))
            else:
                matrix[i].append(0)
    return matrix

def main():
    check_input(sys.argv[0])
    sequences = []
    for _, seq in read_fasta(sys.argv[1]):
        sequences.append(seq)
    for row in create_matrix(sequences):
        print(" ".join([str(i) for i in row]))

if __name__ == "__main__":
    main()