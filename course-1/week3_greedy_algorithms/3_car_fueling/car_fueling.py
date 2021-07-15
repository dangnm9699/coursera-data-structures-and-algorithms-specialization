# python3
import sys


def compute_min_refills(distance, tank, stops):
    # write your code here
    n = len(stops)
    stops.insert(0, 0)
    stops.append(distance)
    num = cur = 0
    while cur <= n:
        last = cur
        while cur <= n and stops[cur+1]-stops[last] <= tank:
            cur += 1
        if cur == last:
            return -1
        if cur <= n:
            num += 1
    return num


if __name__ == '__main__':
    d, m, _, *stops = map(int, sys.stdin.read().split())
    # d, m, _, *stops = map(int, input().split())
    print(compute_min_refills(d, m, stops))
