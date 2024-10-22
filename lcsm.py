#!/usr/bin/env python3
"""
Finding a shared motif
Usage: ./lcsm.py [input_file]
"""

import sys
from tools import read_fasta, check_input

def get_substrings(contig, length):
    """
    Given a contig, substring length, return a list of all substrings
    from that contig.
    """
    subs = []
    num_substrings = (len(contig) + 1) - length
    for i in range(num_substrings):
        subs.append(contig[i:i+length])
    return subs

def get_matching(contigs, substrings):
    """
    Given a list of contigs and a list of substrings,
    check if substrings are in all contigs and return first substring
    that does. Return None otherwise.
    """
    for sub in substrings:
        in_all = True
        for c in contigs[1:]:
            if sub not in c:
                in_all = False
        if in_all:
            return sub
    return None

def get_common(contigs, checker):
    """
    Find common contig in a list of contigs. Use a checker sequence
    to search against other contigs.
    """
    for i in range(len(checker), 0, -1):
        subs = get_substrings(checker, i)
        found_common = get_matching(contigs, subs)
        if found_common != None:
            return(found_common)

def main():
    """Find common substring in input sequences."""
    check_input(sys.argv[0])
    contigs = []
    for _, seq in read_fasta(sys.argv[1]):
        contigs.append(seq)
    
    # Check shortest sequence against other sequences
    checker = min(contigs, key=lambda x: len(x))
    print(get_common(contigs, checker))

if __name__ == "__main__":
    main()