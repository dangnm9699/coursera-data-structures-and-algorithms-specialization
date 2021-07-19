# Uses python3
import sys


# def get_majority_element(a, left, right):
#     # O(n)
#     if left == right:
#         return -1
#     if left + 1 == right:
#         return a[left]
#     d = dict()
#     for i in a:
#         if i not in d.keys():
#             d[i] = 1
#         else:
#             d[i] += 1
#     for k in d.keys():
#         if d[k] > (len(a)//2):
#             return 1
#     return -1


def get_majority_element(a, left, right):
    # O(nlogn)
    if left == right:
        return -1
    if left + 1 == right:
        return a[left]
    # merge sort or quick sort
    # simply use built-in sorted
    a = sorted(a)
    m = (len(a) - 1) // 2
    count = 0
    for i in range(m):
        if a[i] == a[m]:
            count += 1
    for i in range(m, len(a)):
        if a[i] == a[m]:
            count += 1
    if count > (len(a)//2):
        return 1
    return -1


if __name__ == '__main__':
    n = int(input())
    a = list(map(int, input().split()))
    if get_majority_element(a, 0, n) != -1:
        print(1)
    else:
        print(0)
