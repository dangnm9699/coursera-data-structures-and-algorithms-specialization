# Uses python3
import sys


def gcd_naive(a, b):
    if b == 0:
        return a
    return gcd_naive(b, a % b)


def lcm_naive(a, b):
    return (a*b) // gcd_naive(a, b)


if __name__ == '__main__':
    input = sys.stdin.read()
    a, b = map(int, input.split())
    if a < b:
        a, b = b, a
    print(lcm_naive(a, b))
