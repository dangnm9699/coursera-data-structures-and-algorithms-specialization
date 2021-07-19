# Uses python3
import sys


def binary_search(a, x):
    left, right = 0, len(a)
    # write your code here


def linear_search(a, x):
    l = 0
    r = len(a) - 1
    while l <= r:
        m = (l+r)//2
        if a[m] == x:
            return m
        elif a[m] > x:
            r = m - 1
        else:
            l = m + 1
    return -1


if __name__ == '__main__':
    line1 = list(map(int, input().split()))
    line2 = list(map(int, input().split()))
    n = line1[0]
    m = line2[0]
    a = line1[1:]
    for x in line2[1:]:
        # replace with the call to binary_search when implemented
        print(linear_search(a, x), end=' ')
