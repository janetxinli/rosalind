#!/usr/bin/env python3
"""
Finding a protein motif
Usage: ./mprt.py [input file]
"""

import sys
from urllib.request import urlopen
from urllib.error import HTTPError
from tools import read_fasta
from tools import check_input

def is_nglyc(prot_string):
    """
    Takes a 4 amino acid long string, and checks whether the string is an
    N-glycosylation motif or not (N{P}[ST]{P}). Returns a boolean.
    """
    return prot_string[0] == "N" and prot_string[1] != "P" and \
        prot_string[2] in "ST" and prot_string[3] != "P"

def find_domains(uniprot_id):
    """
    Takes as input a uniprot ID, and opens and loads the fasta sequence of that ID.
    Searches all 4-mers within the protein sequence, and if an N-glycosylation domain
    exists within the sequence, prints the ID and positions of the sequences.
    """
    positions = []
    link = "http://www.uniprot.org/uniprot/%s.fasta" % uniprot_id

    # Try to open and load sequence
    try:
        fh = urlopen(link)
        uniprot_fa = fh.read().decode('utf-8').strip().split("\n")
        seq = "".join(uniprot_fa[1:])
        for i in range(len(seq) - 4):
            if is_nglyc(seq[i:i + 4]):
                positions.append(i + 1)
        if len(positions) > 0:
            print(uniprot_id)
            print(" ".join(str(x) for x in positions))

    # If an ID url can't be opened, print out ID
    except HTTPError:
        print(uniprot_id, "could not be opened.")

def main():
    """Search for protein motifs in input."""
    check_input(sys.argv[0])
    with open(sys.argv[1]) as infile:
        for protein_id in infile:
            find_domains(protein_id.strip())

if __name__ == "__main__":
    main()
