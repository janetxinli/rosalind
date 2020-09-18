#!/usr/bin/env python3
"""
Mendel's first law
Usage: ./iprb.py [input data]
"""

import sys
from tools import check_input

def calculate_dom(k, m, n):
    """
    Calculate the probability of two random organisms producing an
    individual possessing a dominant allele.
    """
    total = k + m + n
    second_total = k + m + n - 1

    # First k
    k_k = (k/total) * ((k-1)/second_total)
    k_m = (k/total) * (m/second_total)
    k_n = (k/total) * (n/second_total)
    k_prob = k_k + k_m + k_n

    # First m
    m_k = (m/total) * (k/second_total)
    m_m = 0.75 * (m/total) * ((m-1)/second_total)
    m_n = 0.5 * (m/total) * (n/second_total)
    m_prob = m_k + m_m + m_n

    # First n
    n_k = (n/total) * (k/second_total)
    n_m = 0.5 * (n/total) * (m/second_total)
    n_prob = n_k + n_m
    
    return k_prob + m_prob + n_prob

def main():
    """Calculate probability for input."""
    check_input(sys.argv[0])
    with open(sys.argv[1]) as infile:
        n1, n2, n3 = infile.readline().strip().split(" ")
        print(calculate_dom(int(n1), int(n2), int(n3)))

if __name__ == "__main__":
    main()



