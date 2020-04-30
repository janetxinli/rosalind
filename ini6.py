#!/usr/bin/env python3

def occurences(s):
    words = s.split(' ')
    occ = {}
    for word in words:
        if word in occ:
            occ[word] += 1
        else:
            occ[word] = 1
    for key, value in occ.items():
        print(key, value)
    return