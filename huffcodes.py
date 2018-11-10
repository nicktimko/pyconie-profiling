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

    return {w: {"word": w, "count": word_counts[w], "code": codebook[w]} for w in word_counts}


def report(codes, n=10):
    most_common = heapq.nlargest(n, codes.values(), key=lambda c: c["count"])

    print(f'{"word":>10s} | {"count":>6s} | {"code":>10s}')
    print('-' * 40)
    for info in most_common:
        print(f'{info["word"]:>10s} | {info["count"]:>6d} | {info["code"]:>10s}')


def main(argv=None):
    if argv is None:
       argv = sys.argv[1:]

    parser = argparse.ArgumentParser(description=__doc__)
    # parser.add_argument("-v", "--verbose", action="store_true")
    parser.add_argument("corpus")
    args = parser.parse_args(argv)

    with open(args.corpus) as f:
        text = f.read()

    codes = generate_codes(text, verbose=True)

    report(codes)


if __name__ == "__main__":
    sys.exit(main())
