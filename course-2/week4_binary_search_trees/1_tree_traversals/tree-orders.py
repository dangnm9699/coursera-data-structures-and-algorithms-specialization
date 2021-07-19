# python3

import sys, threading

sys.setrecursionlimit(10 ** 6)  # max depth of recursion
threading.stack_size(2 ** 27)  # new thread will get stack of such size


class TreeOrders:
    def read(self):
        self.n = int(sys.stdin.readline())
        self.key = [0 for i in range(self.n)]
        self.left = [0 for i in range(self.n)]
        self.right = [0 for i in range(self.n)]
        for i in range(self.n):
            [a, b, c] = map(int, sys.stdin.readline().split())
            self.key[i] = a
            self.left[i] = b
            self.right[i] = c

    def inOrder(self):
        self.result = []
        # Finish the implementation
        # You may need to add a new recursive method to do that
        self._inOrder()
        return self.result

    def _inOrder(self, idx=0):
        if self.left[idx] != -1:
            self._inOrder(self.left[idx])
        self.result.append(self.key[idx])
        if self.right[idx] != -1:
            self._inOrder(self.right[idx])
        pass

    def preOrder(self):
        self.result = []
        # Finish the implementation
        # You may need to add a new recursive method to do that
        self._preOrder()
        return self.result

    def _preOrder(self, idx=0):
        self.result.append(self.key[idx])
        if self.left[idx] != -1:
            self._preOrder(self.left[idx])
        if self.right[idx] != -1:
            self._preOrder(self.right[idx])
        pass

    def postOrder(self):
        self.result = []
        # Finish the implementation
        # You may need to add a new recursive method to do that
        self._postOrder()
        return self.result

    def _postOrder(self, idx=0):
        if self.left[idx] != -1:
            self._postOrder(self.left[idx])
        if self.right[idx] != -1:
            self._postOrder(self.right[idx])
        self.result.append(self.key[idx])

        pass


def main():
    tree = TreeOrders()
    tree.read()
    print(" ".join(str(x) for x in tree.inOrder()))
    print(" ".join(str(x) for x in tree.preOrder()))
    print(" ".join(str(x) for x in tree.postOrder()))


threading.Thread(target=main).start()
