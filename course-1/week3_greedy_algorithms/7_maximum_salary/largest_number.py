# Uses python3

import sys


def largest_number(a):
    # write your code here
    ans = ""
    while a:
        max = a[0]
        for s in a[1:]:
            if is_greater_or_equal(s, max):
                max = s
        ans += str(max)
        a.remove(max)
    return ans


def is_greater_or_equal(s1, s2):
    str1 = str(s1)
    str2 = str(s2)
    cc1 = str1 + str2
    cc2 = str2 + str1
    return int(cc1) >= int(cc2)


if __name__ == '__main__':
    input()
    a = list(map(int, input().split()))
    print(largest_number(a))
