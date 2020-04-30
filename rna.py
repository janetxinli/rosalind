#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jul  5 13:41:06 2019

@author: janetli
"""

def rna(dna_string):
    trans_string = ''
    for nuc in dna_string:
        if nuc == 'T':
            trans_string += 'U'
        else:
            trans_string += nuc
    return trans_string

