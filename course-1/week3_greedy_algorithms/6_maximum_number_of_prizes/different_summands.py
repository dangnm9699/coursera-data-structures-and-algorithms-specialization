# Uses python3
import sys


def optimal_summands(n):
    summands = []
    # write your code here
    sum = 0
    add = 1
    while True:
        sum += add
        if sum <= n:
            summands.append(add)
        else:
            sum -= add
            break
        add += 1
    summands[-1] = n - (sum - summands[-1])
    return summands


if __name__ == '__main__':
    n = int(input())
    summands = optimal_summands(n)
    print(len(summands))
    for x in summands:
        print(x, end=' ')
