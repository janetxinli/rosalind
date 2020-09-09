#!/usr/bin/env python3
"""Scan a fasta file given in Rosalind format to yield the header and sequence."""

def read_fasta(filename):
    """
    Takes in a list containing the contents of a file and returns the header and sequence
    of that file in a tuple.
    """

    with open(filename, "r") as fh:
        header = []
        seq = []

        current = fh.readline()

        # Iterate over each line in file object
        while current:
            if current[0] == ">":  # Header line
                header.append(current[1:].strip())
                seq.append("")
            else:  # Sequence line
                seq[-1] += current.strip()

            current = fh.readline()

        # Yield corresponding headers and sequences as tuple
        i = 0
        while i < len(header):
            yield header[i], seq[i]
            i += 1

