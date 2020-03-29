#!/usr/bin/env python3

import sys

def pattern_count(text, pattern):
    count = 0
    for i in range(len(text)-len(pattern)):
        if text[i:i+len(pattern)] == pattern:
            count += 1
    return count

if __name__ == "__main__":
    for i, line in enumerate(sys.stdin):
        if i == 0: # First line in file; represents sequence
            text = line.strip()
#            print(text)
        elif i == 1: # Second line in file; represents pattern
            pattern = line.strip()
#            print(line)
    print(pattern_count(text, pattern), file=sys.stdout)
#    print(pattern_count("ABCADAB", "AB"), file=sys.stdout)

