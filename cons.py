#!/usr/bin/env python3
"""
Consensus and profile.
Usage: python3 ./cons.py [input_file]
"""

import sys
from random import choice
from tools import read_fasta

BASES = ["A", "C", "G", "T"]

def generate_profile(infile):
    """
    Given a fasta file of equal length sequences, return a profile matrix representing
    the number of occurrences of each base.
    """
    seqs = []
    for _, seq in read_fasta(infile):
        seqs.append(seq)

    # Make a profile for nucleotide counts
    profile = []
    for _ in range(len(seqs[0])):
        profile.append([0] * 4)

    # Iterate over every sequence
    for sequence in seqs:
        # Iterate over every character in sequence
        for i in range(len(sequence)):
            if sequence[i] == "A":
                profile[i][0] += 1
            elif sequence[i] == "C":
                profile[i][1] += 1
            elif sequence[i] == "G":
                profile[i][2] += 1
            elif sequence[i] == "T":
                profile[i][3] += 1

    return profile

def get_max(nuc_count):
    """
    Given a list of nucleotide counts [A, T, C, G], return the nucleotide
    that occurs most frequently. If two or more nucleotides are present in equal
    amounts, choose randomly between those nucleotides.
    """

    # Find most frequent base
    most_frequent = max(nuc_count)

    # More than one base is most frequent
    if nuc_count.count(most_frequent) > 1:
        frequent_bases = []
        for i, base in enumerate(nuc_count):
            if base == most_frequent:
                frequent_bases.append(BASES[i])

        # Randomly choose from most frequent bases
        consensus_base = choice(frequent_bases)

    else:
        # Consensus base is most frequent base
        consensus_base = BASES[nuc_count.index(most_frequent)]

    return consensus_base


def get_consensus(profile):
    """
    Given a profile matrix of nucleotide frequencies, return the
    consensus sequence.
    """

    consensus_seq = ""
    for position in range(len(profile)):
        consensus_seq += get_max(profile[position])

    return consensus_seq

def print_profile(profile):
    """
    Print profile matrix so each line displays the counts for a single nucleotide
    in each position of profile.
    """

    for base in range(len(BASES)):
        counts = []
        for pos in range(len(profile)):
            counts.append(str(profile[pos][base]))
        print("{base}: {counts}".format(base=BASES[base], counts=" ".join(counts)))

def main():
    input = sys.argv[1]
    profile_matrix = generate_profile(input)
    print(get_consensus(profile_matrix))
    print_profile(profile_matrix)

if __name__ == "__main__":
    main()


