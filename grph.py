#!/usr/bin/env python3
"""
Overlap Graphs

Given a fasta file of DNA strings, returns all edges (as adjacency lists) corresponding to O3 (strings with overlaps
of 3 base pairs.
"""

import sys
from igraph import Graph, plot
from read_fasta import read_fasta

def prefix(dna_string):
    """Returns the 3 nucleotide long prefix of dna_string."""

    return dna_string[:3]

def suffix(dna_string):
    """Returns the 3 nucleotide long suffix of dna_string."""

    return dna_string[-3:]

def main(infile):
    """Loads all sequences from the input fasta file..."""

    # Create a dictionary holding headers and sequences
    sequences = {}

    # Create a graph holding overlaps
    overlaps = Graph()

    for header, seq in read_fasta(infile):
        sequences[header] = seq

    for header_1 in sequences:
        for header_2 in sequences:
            # Only compare different strings
            if sequences[header_1] != sequences[header_2]:
                # Print headers if suffix of first matches prefix of second
                if suffix(sequences[header_1]) == prefix(sequences[header_2]):
                    print(header_1, header_2, file=sys.stdout)

                    if 'name' in overlaps.vs.attributes():
                        if header_1 not in overlaps.vs['name']:
                            overlaps.add_vertex(header_1)
                        if header_2 not in overlaps.vs['name']:
                            overlaps.add_vertex(header_2)
                    else:
                        overlaps.add_vertex(header_1)
                        overlaps.add_vertex(header_2)

                    overlaps.add_edge(header_1, header_2)

    plot(overlaps)

if __name__ == "__main__":
    main("rosalind_grph.txt")
