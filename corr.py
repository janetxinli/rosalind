#!/usr/bin/env python3
"""
Error correction in reads
Usage: ./corr.py [input file]
"""

import sys
from tools import read_fasta
from hamm import hamming_distance
from revc import rev_comp

def find_erroneous_reads(reads):
    """Given a list of reads, return a list containing tuples of the
    erroneous reads and their corrected reads."""
    read_pairs = []
    correct_reads = set()
    erroneous_reads = set()
    
    for i, first_read in enumerate(reads):
        j = 0
        match = False
        while j < len(reads) and not match:
            if i != j:
                second_read = reads[j]
                second_rev = rev_comp(second_read)
                if first_read == second_read or first_read == second_rev:
                    correct_reads.update([first_read, second_read])
                    match = True
            j += 1
        if not match:
            erroneous_reads.add(first_read)

    # Only want to compare erroneous reads to the correct reads
    for wrong_read in erroneous_reads:
        for correct_read in correct_reads:
            correct_rev = rev_comp(correct_read)
            if hamming_distance(wrong_read, correct_read) == 1:
                read_pairs.append([wrong_read, correct_read])
                break
            elif hamming_distance(wrong_read, correct_rev) == 1:
                read_pairs.append([wrong_read, correct_rev])
                break
    
    return read_pairs

def main():
    if len(sys.argv) != 2:
        print("Usage: %s [input file]" % sys.argv[0])
        sys.exit(1)
    reads = []
    for _, seq in read_fasta(sys.argv[1]):
        reads.append(seq)
    corrected_reads = find_erroneous_reads(reads)
    for pair in corrected_reads:
        print("->".join(pair))

if __name__ == "__main__":
    main()