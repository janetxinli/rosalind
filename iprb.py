#!/usr/bin/env python3
"""
Given k=homozygous dominant, m=heterozygous, n=homozygous recessive, calculate the possibility that two randomly selected
individuals will produce an offspring possessing a dominant allele.

Usage: cat [rosalind.txt] | python3 iprb.py
"""

import sys

def calculate_dom(k, m, n):
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

def run():
    if __name__ == "__main__":
        for line in sys.stdin:
            n1, n2, n3 = line.split(" ")
            n1 = int(n1)
            n2 = int(n2)
            n3 = int(n3)
            print(calculate_dom(n1, n2, n3))

run()



