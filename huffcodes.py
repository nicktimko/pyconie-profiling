#!/usr/bin/env python
"""
Generate Huffman codes from some text file corpus
"""

import argparse
import collections
import heapq
import re
import sys

import huffman


with open('stopwords.txt') as f:
    STOPWORDS = {line.strip() for line in f}


def generate_codes(text, verbose=False):
    text = text.lower()

    words = (groups[0] for groups in re.findall("([a-z]+(['-][a-z]+)*)", text))
    words = (w for w in words if w not in STOPWORDS)
    word_counts = collections.Counter(words)

    codebook = huffman.codebook(word_counts.items())

    shortest_codes = heapq.nsmallest(15, codebook.items(), key=lambda c: len(c[1]))

    # reporting
    if not verbose:
        return

    print(f'{"count":>10s} | {"word"}')
    print('-' * 20)
    for word, count in word_counts.most_common(15):
        print(f'{count:>10d} | {word}')

    print(f'\n{"code":>10s} | {"word"}')
    print('-' * 20)
    for word, code in shortest_codes:
        print(f'{code:>10s} | {word}')


def main(argv=None):
    if argv is None:
       argv = sys.argv[1:]

    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("-v", "--verbose", action="store_true")
    parser.add_argument("corpus")
    args = parser.parse_args(argv)

    with open(args.corpus) as f:
        text = f.read()

    generate_codes(text, verbose=args.verbose)


if __name__ == "__main__":
    sys.exit(main())
