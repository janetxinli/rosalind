#!/usr/bin/env python3
"""
Finding a shared spliced motif
Usage: ./lcsq.py [input file]
"""

import sys
from tools import check_input, read_fasta

def find_common_subsequence(string_1, string_2):
    """Returns the longest common subsequence in string1 and string2."""
    length_1 = len(string_1)
    length_2 = len(string_2)
    
    string_matrix = []  # Store matches in a matrix
    for _ in range(length_1 + 1):
        string_vector = []
        for _ in range(length_2 + 1):
            string_vector.append(0)
        string_matrix.append(string_vector)
    
    row = 1
    while row <= length_1:
        column = 1
        while column <= length_2:
            if string_1[row-1] == string_2[column-1]:
                string_matrix[row][column] = string_matrix[row-1][column-1] + 1
            else:
                string_matrix[row][column] = max(string_matrix[row-1][column], string_matrix[row][column-1])
            column += 1
        row += 1

    subseq = ""
    row_pos, column_pos = length_1, length_2
    score = string_matrix[row_pos][column_pos]
    while score > 0:
        above = string_matrix[row_pos-1][column_pos]
        left = string_matrix[row_pos][column_pos-1]
        if above == score:
            row_pos -= 1
            continue
        elif left == score:
            column_pos -= 1
            continue
        else:
            subseq = string_1[row_pos-1] + subseq
            row_pos -= 1
            column_pos -= 1
            score = string_matrix[row_pos][column_pos]
    
    return subseq

def main():
    """Find longest common subsequence of input sequences."""
    check_input(sys.argv[0])
    seqs = []
    for _, seq in read_fasta(sys.argv[1]):
        seqs.append(seq)
    
    print(find_common_subsequence(seqs[0], seqs[1]))

if __name__ == "__main__":
    main()
