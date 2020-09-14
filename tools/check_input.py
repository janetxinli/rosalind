#!/usr/bin/env python3
"""
Check that the rosalind input file has been provided as an argument.
"""

import sys

def check_input(filename):
    """Check for two command-line arguments: the script itself and 
    the rosalind input file."""
    
    if len(sys.argv) != 2:
        print("Usage: %s [input file]" % filename)
        sys.exit(1)