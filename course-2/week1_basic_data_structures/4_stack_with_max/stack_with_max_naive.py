# python3
import sys


class StackWithMax():
    def __init__(self):
        self.__stack = []
        # auxiliary stack
        self.__aux = []

    def Push(self, a):
        self.__stack.append(a)
        if len(self.__aux) == 0:
            self.__aux.append(a)
        elif a >= self.__aux[-1]:
            self.__aux.append(a)

    def Pop(self):
        assert(len(self.__stack))
        popped = self.__stack.pop()
        if popped == self.__aux[-1]:
            self.__aux.pop()

    def Max(self):
        assert(len(self.__stack))
        return self.__aux[-1]


if __name__ == '__main__':
    stack = StackWithMax()

    num_queries = int(sys.stdin.readline())
    for _ in range(num_queries):
        query = sys.stdin.readline().split()

        if query[0] == "push":
            stack.Push(int(query[1]))
        elif query[0] == "pop":
            stack.Pop()
        elif query[0] == "max":
            print(stack.Max())
        else:
            assert(0)
