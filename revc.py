#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Return reverse complement of a dna strand
"""

def rev_comp(dna_strand):

    new_strand = ''
    for nuc in dna_strand:
        if nuc == 'A':
            new_strand = 'T' + new_strand
        elif nuc == 'T':
            new_strand = 'A'+ new_strand
        elif nuc == 'G':
            new_strand = 'C' + new_strand
        elif nuc == 'C':
            new_strand = 'G' + new_strand
    return new_strand

# print(rev_comp("ATATA"))
# print(rev_comp("AAAAA"))


