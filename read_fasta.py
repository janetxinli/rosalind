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
    header = []
    seq = []

    current = file_obj.readline()
    current_seq = None

    # Iterate over each line in file object
    while current:
        # current_seq = None
        # Header line
        if current[0] == ">":
            if current_seq:
                seq.append(current_seq)
            current_seq = None
            header.append(current[1:].strip())

        # First sequence line
        elif not current_seq:
            current_seq = current.strip()

        else:
            current_seq += current.strip()

        current = file_obj.readline()

    # Append last sequence to seq list
    seq.append(current_seq)

    while len(header) > 0 and len(seq) > 0:
        yield header.pop(0), seq.pop(0)

