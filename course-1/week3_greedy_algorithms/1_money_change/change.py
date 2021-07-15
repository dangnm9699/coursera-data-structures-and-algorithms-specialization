# Uses python3
import sys


def get_change(m):
    # write your code here
    res = 0
    for i in [10, 5, 1]:
        res += (m//i)
        m %= i
    return res


if __name__ == '__main__':
    m = int(sys.stdin.read())
    # m = int(input())
    print(get_change(m))
