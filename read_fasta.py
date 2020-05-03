#!/usr/bin/env python3
"""
Scan a fasta file given in Rosalind format and return the header (position 0)
and sequence (position 1)
"""

def read_fasta(file_obj):
    """
    Takes in a list containing the contents of a file and returns the header and sequence
    of that file in a tuple.
    """
    header = ""
    seq = ""

    for line in file_object:
        if line[0] == ">":
            header += line.strip()
        else:
            seq += line.strip()

    return header, seq