#!/usr/bin/env python3
"""
Consensus and profile.
Usage: ./cons.py [input file]
"""

import sys
from random import choice
from tools import read_fasta, check_input

BASES = ["A", "C", "G", "T"]

def generate_profile(seqs):
    """
    Given a fasta file of equal length sequences, return a profile matrix representing
    the number of occurrences of each base.
    """
    profile = []
    for _ in range(len(seqs[0])):
        profile.append([0] * 4)

    for sequence in seqs:
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
    most_frequent = max(nuc_count)
    if nuc_count.count(most_frequent) > 1:
        frequent_bases = []
        for i, base in enumerate(nuc_count):
            if base == most_frequent:
                frequent_bases.append(BASES[i])
        consensus_base = choice(frequent_bases)
    else:
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
    """Print consensus sequence and profile matrix for a given set of sequences."""
    check_input(sys.argv[0])
    infile = sys.argv[1]
    seqs = []
    for _, seq in read_fasta(infile):
        seqs.append(seq)
    profile = generate_profile(seqs)
    print(get_consensus(profile))
    print_profile(profile)

if __name__ == "__main__":
    main()


