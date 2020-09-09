#!/usr/bin/env python3

import sys
from tools import read_fasta

def quaternary_to_decimal(quaternary):
    """Convert a string representing a quaternary number to a decimal number."""
    total = 0
    quaternary_list = list(quaternary)
    i = 0
    while len(quaternary_list) > 0:
        total += int(quaternary_list.pop()) * (4**i)
        i += 1
    return total

def kmer_to_index(kmer):
    """Given a kmer, return the corresponding lexicographical index."""
    BASE_NUM = {"A": "0", "C": "1", "G": "2", "T": "3"}
    quaternary_kmer = ""    
    for base in kmer:
        quaternary_kmer += BASE_NUM[base]
    return quaternary_to_decimal(quaternary_kmer)

def count_composition(sequence):
    """Count the 4-mer composition of a sequence."""
    composition = [0] * 256  # 256 possible 4-mers of an alphabet of 4 letters
    i = 0
    while i <= len(sequence) - 4:
        composition[kmer_to_index(sequence[i:i+4])] += 1
        i += 1
    print(" ".join([str(x) for x in composition]))

def main():
    if len(sys.argv) != 2:
        print("Usage: %s [input file]" % sys.argv[0])
        sys.exit(1)
    for _, seq in read_fasta(sys.argv[1]):
        count_composition(seq)

if __name__ == "__main__":
    main()