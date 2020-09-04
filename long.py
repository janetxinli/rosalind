#!/usr/bin/env python3
# Usage: python3 long.py <infile>

import sys
from graph import Graph
from read_fasta import read_fasta

def suffix(sequence, l):
    """Returns the suffix of length l of a string sequence."""
    if l > len(sequence):
        return sequence
    else:
        return sequence[-l:]

def prefix(sequence, l):
    """Returns the prefix of length l of a string sequence."""
    if l > len(sequence):
        return sequence
    else:
        return sequence[:l]

def create_graph(list_of_seq):
    """Creates an overlap graph based on a list of sequences."""
    super_string_graph = Graph()
    num_seq = len(list_of_seq)
    i = 0
    while i < num_seq:
        first = list_of_seq[i]
        j = 0
        while j < num_seq:
            if i != j:
                second = list_of_seq[j]
                max_overlap = min(len(first), len(second))  # Maximum overlength is shortest sequence
                min_overlap = max(len(first), len(second)) // 2 # Minimum overlap is half of the largest sequence
                overlap = max_overlap
                found = False
                while overlap >= min_overlap and not found:
                    if suffix(first, overlap) == prefix(second, overlap):
                        super_string_graph.add_edge(first, second, weight=overlap)
                        found = True
                    overlap -= 1
            j += 1
        i += 1
    return super_string_graph

def find_shortest_superstring(sequence_graph):
    """Finds the shortest superstring of a given graph."""
    superstring = ""
    for v in sequence_graph:
        if v.indegree == 0:
            current = v
            superstring += current.name
            next = current.get_edge()
            while next:
                current_seq = current.name
                next_seq = next.name
                max_overlap = min(len(current_seq), len(next_seq))
                min_overlap = max(len(current_seq), len(next_seq)) // 2
                overlap = max_overlap
                found = False
                while overlap >= min_overlap and not found:
                    if suffix(current_seq, overlap) == prefix(next_seq, overlap):
                        superstring += suffix(next_seq, len(next_seq) - overlap)
                        current = next
                        if next.has_edges():
                            next = next.get_edge()
                        else:
                            next = None
                        found = True
                    overlap -= 1
    return superstring

def main():
    infile = sys.argv[1]
    seqs = []
    for _, seq in read_fasta(infile):
        seqs.append(seq)
    graph = create_graph(seqs)
    print(find_shortest_superstring(graph))


if __name__ == "__main__":
    main()
