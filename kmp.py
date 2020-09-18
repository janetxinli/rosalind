#!/usr/bin/env python3
"""
Speeding up motif finding
Usage: ./kmp.py [input file]
"""

import sys
from tools import read_fasta, check_input
from long import prefix

def create_failure_array(sequence):
    """Produce the failure array for a given sequence."""
    seq_length = len(sequence)
    failure = [0] * seq_length
    i = 1
    while i < seq_length:
        prev_score = failure[i-1]
        if prev_score == 0 and sequence[i] == sequence[0]:
            failure[i] += 1
        elif prev_score > 0:
            if sequence[i] == sequence[prev_score]:
                failure[i] = prev_score + 1
            else:
                j = prev_score
                while j > 0:
                    if sequence[i-j+1:i+1] == prefix(sequence, j):
                        failure[i] = j
                        break
                    j -=1
        i += 1
    
    return failure

def main():
    """Read file and print the failure array."""
    check_input(sys.argv[0])
    for _, seq in read_fasta(sys.argv[1]):
        print(" ".join([str(x) for x in create_failure_array(seq)]))
    

if __name__ == "__main__":
    main()