"""
Classic recursive Fibonacci
"""
import sys


def fib(n):
    if n <= 2:
        return 1
    return fib(n - 2) + fib(n - 1)


def main():
    n = int(sys.argv[1])

    print(fib(n))


if __name__ == "__main__":
    main()
