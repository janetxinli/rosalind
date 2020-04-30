#!/usr/bin/env python3

def odd_lines(filename):
    file = open(filename, 'r')
    new = open('newfile','w')
    line_no = 0
    for line in file:
        line_no += 1
        if line_no % 2 == 0:
            new.write(line)
    file.close()
    new.close()
    return