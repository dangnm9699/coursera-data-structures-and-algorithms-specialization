# python3

import sys


class Solver:
    def __init__(self, s):
        self.s = s
        self.m1 = 1000000007
        self.m2 = 1000000009
        self.x = 263
        self.h1 = [0] * (len(self.s) + 1)
        self.h2 = [0] * (len(self.s) + 1)
        for i in range(1, len(self.s) + 1):
            self.h1[i] = (self.x * self.h1[i - 1] + ord(self.s[i - 1])) % self.m1
            self.h2[i] = (self.x * self.h2[i - 1] + ord(self.s[i - 1])) % self.m2

    def ask(self, a, b, l):
        h1_a = (self.h1[a + l] - pow(self.x, l, self.m1) * self.h1[a]) % self.m1
        h1_b = (self.h1[b + l] - pow(self.x, l, self.m1) * self.h1[b]) % self.m1
        h2_a = (self.h2[a + l] - pow(self.x, l, self.m2) * self.h2[a]) % self.m2
        h2_b = (self.h2[b + l] - pow(self.x, l, self.m2) * self.h2[b]) % self.m2
        return h1_a == h1_b and h2_a == h2_b


s = sys.stdin.readline()
q = int(sys.stdin.readline())
solver = Solver(s)
for i in range(q):
    a, b, l = map(int, sys.stdin.readline().split())
    print("Yes" if solver.ask(a, b, l) else "No")
