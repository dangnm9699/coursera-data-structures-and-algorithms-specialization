# Uses python3
import sys
import random


def partition3(a, l, r):
    # write your code here
    x = a[l]
    j = l
    for i in range(l+1, r + 1):
        if a[i] == x:
            j += 1
            a[i], a[j] = a[j], a[i]
    be = j + 1
    for i in range(be, r + 1):
        if a[i] < x:
            j += 1
            a[i], a[j] = a[j], a[i]
    fi = j
    id = l
    for i in range(be, fi + 1):
        a[i], a[id] = a[id], a[i]
        id += 1
    return id, fi


def partition2(a, l, r):
    x = a[l]
    j = l
    for i in range(l + 1, r + 1):
        if a[i] <= x:
            j += 1
            a[i], a[j] = a[j], a[i]
    a[l], a[j] = a[j], a[l]
    return j


def randomized_quick_sort(a, l, r):
    if l >= r:
        return
    k = random.randint(l, r)
    a[l], a[k] = a[k], a[l]
    # use partition3
    # partition3(a, l, r)
    m, n = partition3(a, l, r)
    randomized_quick_sort(a, l, m - 1)
    randomized_quick_sort(a, n + 1, r)


if __name__ == '__main__':
    n = int(input())
    a = list(map(int, input().split()))
    randomized_quick_sort(a, 0, n - 1)
    for x in a:
        print(x, end=' ')
