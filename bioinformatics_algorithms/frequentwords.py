#!/usr/bin/env python3

from patterncount import pattern_count

def frequent_words(text, k):
    frequent_patterns = set()
    count = [0] * (len(text)-k+1)
    for i in range(len(text)-k):
        count[i] = pattern_count(text, text[i:i+3])
    max_count = max(count)
    for i in range(len(text)-k):
        if count[i] == max_count:
            frequent_patterns.add(text[i:i+3])
    return frequent_patterns



