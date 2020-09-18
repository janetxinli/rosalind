#!/usr/bin/env python3
"""
Computing GC content
Usage: ./gc.py [input file]
"""

import sys
from tools import read_fasta, check_input

def get_gc(seq):
    """Get the GC content for a given sequence."""
    gc_count = 0
    for base in seq:
        if base == "G" or base == "C":
            gc_count += 1
    return (gc_count/len(seq)) * 100

def main():
    """Print GC content for input sequence."""
    check_input(sys.argv[0])
    gc_content = {}
    for header, seq in read_fasta(sys.argv[1]):
        gc_content[get_gc(seq)] = header
    max_gc = max(gc_content)
    print(gc_content[max_gc])
    print(max_gc)

if __name__ == "__main__":
    main()
