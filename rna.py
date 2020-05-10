#!/usr/bin/env python3
"""
Given an input dna string, transcribe and return the corresponding rna string.
"""

def rna(dna_string):
    trans_string = ''
    for nuc in dna_string:
        if nuc == 'T':
            trans_string += 'U'
        else:
            trans_string += nuc
    return trans_string

