#!/usr/bin/env python3
"""
Takes a file containing a different uniprot ID on each line from stdin and prints the IDs containing
N-glycosylation domains and their respective locations (1-based indexing) to stdout.
"""

import sys
from urllib.request import urlopen
from urllib.error import HTTPError
from read_fasta import read_fasta

def is_nglyc(prot_string):
    """
    Takes a 4 amino acid long string, and checks whether the string is an
    N-glycosylation motif or not (N{P}[ST]{P}). Returns a boolean.
    """

    is_nglyc_motif = True

    if prot_string[0] != "N":
        is_nglyc_motif = False
    elif prot_string[1] == "P":
        is_nglyc_motif = False
    elif prot_string[2] not in "ST":
        is_nglyc_motif = False
    elif prot_string[3] == "P":
        is_nglyc_motif = False

    return is_nglyc_motif

def find_domains(uniprot_id):
    """
    Takes as input a uniprot ID, and opens and loads the fasta sequence of that ID.
    Searches all 4-mers within the protein sequence, and if an N-glycosylation domain
    exists within the sequence, prints the ID and positions of the sequences.
    """

    positions = []

    link = "http://www.uniprot.org/uniprot/{id}.fasta".format(id=uniprot_id)
    # print(urlopen(link).read().decode('utf-8'))

    # Try to open and load sequence
    try:
        fh = urlopen(link)
        uniprot_fa = fh.read().decode('utf-8').strip().split("\n")
        _, seq = read_fasta(uniprot_fa)

        # Iterate over all 4-mers in protein sequence
        for i in range(len(seq) - 4):
            if is_nglyc(seq[i:i + 4]):
                positions.append(i + 1)

        # Return uniprot ID and positions of N-glycosylation domains within protein sequence
        if len(positions) > 0:
            print(uniprot_id)
            print(" ".join(str(x) for x in positions))

    # If an ID url can't be opened, print out ID
    except HTTPError:
        print(uniprot_id, "could not be opened.")

# find_domains("A2Z669")
# find_domains("B5ZC00")

if __name__ == "__main__":
    for prot_id in sys.stdin:
        find_domains(prot_id.strip())
