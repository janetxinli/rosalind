#!/usr/bin/env python3
"""
Given a fasta file, compute GC content and return the sequence with highest GC-content and its ID.
usage: cat [fasta file] | python3 gc.py
Author: janetxinli
"""

import sys

def get_gc(seq):
    gc_count = 0
    gc_count = seq.count("C")
    gc_count += seq.count("G")
    return((gc_count/len(seq)) * 100)

def run_gc():
    gc_content = {}
    last_seq = ""

    # Read first line and load ID
    last_ID = sys.stdin.readline().strip()[1:]

    # Read rest of fasta file
    for line in sys.stdin:
        if line[0] != ">":
            # Load sequence contained in line
            last_seq += line.strip().upper()
        else:
            # Header line; deposit ID and gc content of sequence into gc_content
            last_seq_gc = get_gc(last_seq)
            gc_content[last_seq_gc] = last_ID
            last_seq = ""
            last_ID = line.strip()[1:]

    # Deposit ID and gc content of last sequence into gc_content
    last_seq_gc = get_gc(last_seq)
    gc_content[last_seq_gc] = last_ID

    max_GC = max(gc_content)
    print(gc_content[max_GC], max_GC, sep="\n")
    return

if __name__ == "__main__":
    run_gc()
