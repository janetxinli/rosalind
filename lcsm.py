#!/usr/bin/env python3
"""
Finding a shared motif
Usage: ./lcsm.py [input_file]
"""

import sys

def fasta_to_contigs(infile):
    """
    Takes input file object in fasta format and returns a list
    of all contigs in the file.
    """
    contig = ""
    contig_list = []
    for line in infile:
        if line[0] == ">":  # Header line
            contig_list.append(contig)
            contig = ""
        else:
            contig += line.strip()
    contig_list.append(contig)
    del contig_list[0]
    return contig_list


def get_substrings(contig, length):
    """
    Given a contig, substring length,
    return a list of all substrings from that contig.
    """
    subs = []
    num_substrings = (len(contig) + 1) - length
    for i in range(num_substrings):
        subs.append(contig[i:i+length])
    return subs

# print(get_substrings("CCATA", 3))

def get_matching(contigs, substrings):
    """
    Given a list of contigs and a list of substrings,
    check if substrings are in all contigs and return first substring
    that does. Return False otherwise.
    """
    for sub in substrings:  # Check every possible substring in first contig
        in_all = True  # Present in all contigs so far
        for c in contigs[1:]:  # Every contig after first
            if sub not in c:
                in_all = False
        if in_all:  # If substring is present in all contigs, return substring
            return sub
    return None  # If none of the substrings are present in every contig, return None

# # contigs = [[1,2,3,4,5], [1,2,4]]

if __name__ == "__main__":

    with open(sys.argv[1]) as infile:
        contigs = fasta_to_contigs(infile)

    # Check substrings from first contig
    checker = contigs[0]  # First contig; acts as checker
    for i in range(len(checker), 0, -1):  # Decrease length of substring by 1 each time
        subs = get_substrings(checker, i)
        found_common = get_matching(contigs, subs)
        if found_common != None:
            print(found_common)
            sys.exit(0)