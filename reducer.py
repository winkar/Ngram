#!/usr/bin/env python

import sys
from collections import defaultdict

tri_count = defaultdict(int)
bi_count = defaultdict(int)

if __name__ == '__main__':
    for line in sys.stdin:
        tri_word = tuple(line.split())
        bi_word = tuple(tri_word[:2])
        tri_count[tri_word] += 1
        bi_count[bi_word] += 1
    for key in tri_count:
        tri_word = key
        bi_word = key[:2]
        print bi_count[bi_word], tri_count[tri_word], key[0], key[1], key[2]
