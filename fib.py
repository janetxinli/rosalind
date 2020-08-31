#!/usr/bin/env python3
"""
Fibonacci rabbits and recursion.
"""

def fib_rabbits(months, litter):
    """
    Calculate the number of rabbit pairs present after months if each reproductive
    pair produces a litter of size litter.
    """
    if months == 0:
        return 0
    elif months == 1:
        return 1

    # Every pair reproductive the month before will still be reproductive
    reproductive = fib_rabbits(months - 1, litter)

    # Every pair from two months ago will produce a litter
    young = litter * fib_rabbits(months - 2, litter)
    return reproductive + young

# print(fib_rabbits(6, 1))

def mortal_fib_rabbits(n, m):
    """
    Return the total number of pairs of rabbits that will
    remain after n months if all rabbits life for m months.
    """

    # Create an array holding number of rabbits of each age
    ages = [0] * m
    ages[1] = 1
    month = 3

    if n < 3:
        return 1

    else:

        # Iterate over all months
        while month <= n:

            # Count reproductive age rabbits
            reproductive = 0
            for i in range(1, m):
                reproductive += ages[i]

            # Remove all rabbits of oldest age
            ages[m-1] = 0

            # Shift ages of all rabbits up one
            for i in range(m-1, 0, -1):
                ages[i] += ages[i-1]
                ages[i-1] = 0

            # New young rabbits equal to number of previously reproductive rabbits
            ages[0] += reproductive

            month += 1

    return sum(ages)

# mortal_fib_rabbits(6, 3)
print(mortal_fib_rabbits(90, 20))