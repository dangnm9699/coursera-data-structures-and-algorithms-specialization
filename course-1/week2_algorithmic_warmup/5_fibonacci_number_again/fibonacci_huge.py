# Uses python3
import sys


def pisano(m):
    previous = 0
    current = 1
    result = 0
    for i in range(m*m):
        previous, current = current % m, (current + previous) % m
        if previous == 0 and current == 1:
            result = i + 1
    return result


def get_fibonacci_huge_naive(n, m):

    pisano_period = pisano(m)

    n %= pisano_period

    if n <= 1:
        return n

    previous = 0
    current = 1

    for _ in range(n - 1):
        previous, current = current % m, (previous + current) % m

    return current % m


if __name__ == '__main__':
    input = sys.stdin.read()
    n, m = map(int, input.split())
    print(get_fibonacci_huge_naive(n, m))
