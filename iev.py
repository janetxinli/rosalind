#!usr/bin/env python3
"""
Calclate the expected number of offspring displaying a dominant phenotype
given a population of various genotypes.
"""

expected_dom = {1: 1, 2: 1, 3: 1, 4: 0.75, 5: 0.5, 6: 0}

population = input("What is the sample population? ").split(" ")

def calculate_average(pop_list):
    """
    """
    resulting_dom = 0
    for i, geno in enumerate(pop_list):
        resulting_dom += 2 * int(geno) * expected_dom[i + 1]

    return resulting_dom

print(calculate_average(population))


