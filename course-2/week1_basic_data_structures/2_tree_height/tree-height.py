# python3

import sys, threading
sys.setrecursionlimit(10**7) # max depth of recursion
threading.stack_size(2**27)  # new thread will get stack of such size

class TreeHeight:
    def read(self):
        self.n = int(sys.stdin.readline())
        self.parent = list(map(int, sys.stdin.readline().split()))
        self.my_dict = dict()

    def compute_height(self):
        # Replace this code with a faster implementation
        self.my_dict[-1] = 0
        max_height = 0
        for key in range(self.n):
            max_height = max(max_height, self.height(key=key))
        return max_height

    def height(self, key: int):
        if key in self.my_dict:
            return self.my_dict[key] 
        next_key = self.parent[key]
        height = 1 + self.height(next_key)
        self.my_dict[key] = height
        return height
        

def main():
    tree = TreeHeight()
    tree.read()
    print(tree.compute_height())

threading.Thread(target=main).start()
