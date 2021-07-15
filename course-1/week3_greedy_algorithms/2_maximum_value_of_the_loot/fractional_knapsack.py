# Uses python3
import sys


def get_optimal_value(capacity, weights, values):
    value = 0.
    # write your code here
    a = []
    for i in range(len(weights)):
        a.append((values[i]/weights[i], weights[i]))
    a = sorted(a, key=lambda x: x[0], reverse=True)
    for i in a:
        if capacity == 0:
            return value
        w = min(i[1], capacity)
        capacity -= w
        value += w*i[0]
    return value


if __name__ == "__main__":
    data = list(map(int, sys.stdin.read().split()))
    # data = list(map(int, input().split()))
    n, capacity = data[0:2]
    values = data[2:(2 * n + 2):2]
    weights = data[3:(2 * n + 2):2]
    opt_value = get_optimal_value(capacity, weights, values)
    print("{:.4f}".format(opt_value))
