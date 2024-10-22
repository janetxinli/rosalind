#!/usr/bin/env python3
"""Transitions and transversions
Usage: ./tran.py [input file]
"""

import sys
from tools import check_input, read_fasta

class Base:
    """A base (nucleotide) class."""
    def __init__(self, nucleotide):
        self.nucleotide = nucleotide.upper()
        if self.nucleotide not in "ACTG":
            raise ValueError("Nucleotide must be one of 'A', 'T', 'G', or 'C'")
    
    def type(self):
        if self.nucleotide == "A" or self.nucleotide == "G":
            return "purine"
        elif self.nucleotide == "C" or self.nucleotide == "T":
            return "pyrimidine"

class Mutation():
    """A mutation class that compares bases."""
    def __init__(self, old, new):
        self.old = Base(old)
        self.new = Base(new)
    
    def mutation_type(self):
        if self.old.type() == self.new.type():
            return "transition"
        else:
            return "transversion"

def count_mutations(seq_1, seq_2):
    """Count the number of transitions and transversions between two sequences of equal length."""
    length = len(seq_1)
    transitions = 0
    transversions = 0
    i = 0
    while i < length:
        if seq_1[i] != seq_2[i]:
            if Mutation(seq_1[i], seq_2[i]).mutation_type() == "transition":
                transitions += 1
            else:
                transversions += 1
        i += 1
    
    return transitions, transversions

def main():
    """Count transitions and transversions between two given DNA strings."""
    check_input(sys.argv[0])
    i = 0
    for _, seq in read_fasta(sys.argv[1]):
        if i == 0:
            seq_1 = seq
        elif i == 1:
            seq_2 = seq
        i += 1
    
    transitions, transversions = count_mutations(seq_1, seq_2)
    ratio = transitions / transversions
    print(ratio)

if __name__ == "__main__":
    main()