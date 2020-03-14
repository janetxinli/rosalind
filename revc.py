#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jul  5 13:40:39 2019

@author: janetli
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
