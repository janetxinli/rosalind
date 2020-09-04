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
    length = len(list_of_seq[0])  # Longest sequence length
    middle = length // 2
    pos = length
    num_seq = len(list_of_seq)
    while pos >= middle:
        i = 0
        while i < num_seq:
            found = False
            j = 0
            while j < num_seq and not found:
                first = list_of_seq[i]
                second = list_of_seq[j]
                if i != j and suffix(first, pos) == prefix(second, pos):
                    super_string_graph.add_edge(first, second)
                    found = True
                j += 1
            i += 1
        pos -= 1
    return super_string_graph

def find_shortest_superstring(sequence_graph):
    """Finds the shortest superstring of a given graph."""
    superstring = ""
    for v in sequence_graph:
        if v.indegree == 0:
            # print("start is %s" % v.name)
            current = v
            superstring += current.name
            seq_len = len(current.name)
            middle = seq_len // 2
            next = current.get_edge()
            while next.has_edges():
                # print("%s has edges" % next.name)
                pos = seq_len
                found = False
                while pos >= middle and not found:
                    if suffix(current.name, pos) == prefix(next.name, pos):
                        superstring += suffix(next.name, seq_len-pos)
                        current = next
                        # if next.has_edges():
                        #     next = next.get_edge()
                        # else:
                        #     next = None
                        next = next.get_edge()
                        found = True
                    pos -= 1
    superstring += suffix(next.name, seq_len-pos+1)
    return superstring

if __name__ == "__main__":
    # sequence_graph = create_graph(['ATTAGACCTG', 'CCTGCCGGAA', 'AGACCTGCCG', 'GCCGGAATAC'])
    # print(find_shortest_superstring(sequence_graph))
    infile = sys.argv[1]
    seqs = []
    for _, seq in read_fasta(infile):
        seqs.append(seq)
    print(find_shortest_superstring(create_graph(seqs)))
    # graph = create_graph(seqs)

### Define max overlap and middle for every pair of reads