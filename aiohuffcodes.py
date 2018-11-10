#!/usr/bin/env python
"""
Generate Huffman codes from some text file corpus
"""

import asyncio
import argparse
import sys

import aiohttp

import huffcodes


async def main(argv=None):
    if argv is None:
       argv = sys.argv[1:]

    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("-v", "--verbose", action="store_true")
    parser.add_argument("corpus")
    args = parser.parse_args(argv)

    async with aiohttp.ClientSession() as session:
        async with session.get(args.corpus) as response:
            text = await response.text()

    huffcodes.generate_codes(text, verbose=args.verbose)


if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    sys.exit(loop.run_until_complete(main()))
