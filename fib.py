"""
Classic recursive Fibonacci
"""

import argparse


def fib(n):
    if n <= 2:
        return 1
    return fib(n - 2) + fib(n - 1)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("n", type=int)
    args = parser.parse_args()

    print(fib(args.n))


if __name__ == "__main__":
    main()
