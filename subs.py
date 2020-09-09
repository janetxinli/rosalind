#!/usr/bin/env python3

import sys

def substring_location(string, sub):
    """Given a string and a substring, return all locations of the substring within 
    the string as a list."""
    locations = ""
    for i in range(len(string)-len(sub)+2):
        if string[i:i+len(sub)].upper() == sub.upper():
            locations += str(i+1) + " "
    return locations.strip()

def main():
    """Find substrings."""
    if len(sys.argv) != 2:
        print("Usage: python3 subs.py [rosalind file]", file=sys.stdout)
        sys.exit(1)
    infile = sys.argv[1]
    with open(infile, "r") as infile:
        lines = infile.readlines()
        print(substring_location(lines[0].strip(), lines[1].strip()), file=sys.stdout)

if __name__ == "__main__":
    main()