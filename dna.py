#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jul  5 13:40:40 2019

@author: janetli
"""

def n_count(dna_string):
    a_count = 0
    c_count = 0
    g_count = 0
    t_count= 0
    for nuc in dna_string:
        if nuc.upper() == 'A':
            a_count += 1
        elif nuc.upper() == 'C':
            c_count += 1
        elif nuc.upper() == 'G':
            g_count += 1
        elif nuc.upper() == 'T':
            t_count += 1
        else:
            continue
    return print(a_count, c_count, g_count, t_count)


    