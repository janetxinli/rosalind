#!/usr/bin/env python3
"""
Takes an RNA string s corresponding to a strand of mRNA (<10 kbp), and returns the protein
string encoded by S.
"""

from sys import stdin, stdout

genetic_code = {"UUU":"F", "UUC":"F", "UUA":"L", "UUG":"L", "UCU":"S", "UCA":"S", "UCG":"S", "UCC":"S", \
                "UAU":"Y", "UAC":"Y", "UAA":"Stop", "UAG":"Stop", "UGU":"C", "UGC":"C", "UGA":"Stop", "UGG":"W", \
                "CUU":"L", "CUC":"L", "CUA":"L", "CUG":"L", "CCU":"P", "CCC":"P", "CCA":"P", "CCG":"P", \
                "CAU":"H", "CAC":"H", "CAA":"Q", "CAG":"Q", "CGU":"R", "CGC":"R", "CGA":"R", "CGG":"R",\
                "AUU":"I", "AUC":"I", "AUA":"I", "AUG":"M", "ACU":"T", "ACC":"T", "ACA":"T", "ACG":"T", \
                "AAU":"N", "AAC":"N", "AAA":"K", "AAG":"K", "AGU":"S", "AGC":"S", "AGA":"R", "AGG":"R", \
                "GUU":"V", "GUC":"V", "GUA":"V", "GUG":"V", "GCU":"A", "GCC":"A", "GCA":"A", "GCG":"A", \
                "GAU":"D", "GAC":"D", "GAA":"E", "GAG":"E", "GGU":"G", "GGC":"G", "GGA":"G", "GGG":"G"}

def translate(rna_string):
    if not type(rna_string) is str:
        raise TypeError("Only strings allowed")
    peptide = ""
    codon_list = [rna_string[i:3+i].upper() for i in range (0, len(rna_string), 3)]
    for codon in codon_list:
        if codon == "UAA":
            continue
        elif codon == "UAG":
            continue
        elif codon == "UGA":
            continue
        else:
            peptide += genetic_code[codon]
    return peptide

def run_translate():
    input_string = ""
    for line in stdin:
        input_string += line.strip()
    print(translate(input_string), file=stdout)
    return

if __name__ == "__main__":
    run_translate()