#!/usr/bin/env python3
"""
Fibonacci rabbits and recursion.
"""

def fib_rabbits(months, litter):
    if months == 0:
        return 0
    elif months == 1:
        return 1

    # Every pair reproductive the month before will still be reproductive
    reproductive = fib_rabbits(months - 1, litter)

    # Every pair from two months ago will produce a litter
    young = litter * fib_rabbits(months - 2, litter)
    return reproductive + young


print(fib_rabbits(28, 2))