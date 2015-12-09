#!/usr/bin/env python

import sys
from collections import defaultdict

count = defaultdict(int)

if __name__ == '__main__':
    for line in sys.stdin:
        tri_word = tuple(line.split())
        count[tri_word] += 1
    for key in count:
        print count[key], key[0], key[1], key[2]
