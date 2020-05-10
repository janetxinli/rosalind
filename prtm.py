#!/usr/bin/env python3
"""
Calculate the mass of an input protein.
Usage: cat [protein string] | python3 prtm.py
"""

import sys

def get_amino_acids():
    aa_dict = {}
    with open("aa_mass.txt", "r") as aa_mass:
        for line in aa_mass:
            aa = line.strip().split("   ")
#            print(aa)
            aa_dict[aa[0]] = float(aa[1])

    return aa_dict

def calculate_weight(protein_string, aa_weights):
    total_weight = 0
    for p in protein_string:
        total_weight += aa_weights[p]
    return format(total_weight, ".3f")

# aa_weights = get_amino_acids()
# print(calculate_weight("SKADYEK", aa_weights))

def main():
    aa_weights = get_amino_acids()
    input_protein = ""
    for line in sys.stdin:
        input_protein += line.strip()

    print(calculate_weight(input_protein, aa_weights), file=sys.stdout)

if __name__ == "__main__":
    main()
