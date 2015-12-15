#!/usr/bin/env python
#coding=utf-8

import sys
import re
import HTMLParser

parser = HTMLParser.HTMLParser()

if __name__ == '__main__':
    for line in sys.stdin:
        origin_line = line
        line = line.decode('utf-8')
        line = parser.unescape(line)

        if line.startswith('#') or line.startswith('!'):
            continue

        sentences = re.split(r"[^0-9a-zA-Z\s]", line)
        sentences = [x.strip() for x in sentences if len(x.strip().split()) >= 3]

        for sentence in sentences:
            sentence = sentence.split()
            for tri_word in [sentence[i:i + 3] for i in range(len(sentence) - 3)]:
                tri_word = map(unicode.lower, tri_word)
                print tri_word[0], tri_word[1], tri_word[2]
