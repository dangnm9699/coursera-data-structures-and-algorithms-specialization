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


def fibonacci_sum_naive(n):
    pisano_period = pisano(10)

    m = n // pisano_period
    n %= pisano_period

    if n <= 1:
        return n

    previous = 0
    current = 1
    sum = 1
    aux = 0

    for i in range(pisano_period - 1):
        previous, current = current % 10, (previous + current) % 10
        sum += current
        sum %= 10
        if i + 2 == n:
            aux = sum

    return (sum*m + aux) % 10


if __name__ == '__main__':
    # input = sys.stdin.read()
    n = int(input())
    print(fibonacci_sum_naive(n))
