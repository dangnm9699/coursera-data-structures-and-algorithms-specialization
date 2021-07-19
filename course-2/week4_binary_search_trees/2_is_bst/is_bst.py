#!/usr/bin/python3

import sys, threading

sys.setrecursionlimit(10 ** 9)  # max depth of recursion
threading.stack_size(2 ** 30)  # new thread will get stack of such size


def IsBinarySearchTree(tree):
    # Implement correct algorithm here
    in_order = inorder(tree)
    for i in range(1, len(in_order)):
        if tree[in_order[i]][0] < tree[in_order[i - 1]][0]:
            return False
    return True


def inorder(tree):
    res = []
    _inorder(tree, res)
    return res


def _inorder(tree, res, idx=0):
    if tree[idx][1] != -1:
        _inorder(tree, res, tree[idx][1])
    res.append(idx)
    if tree[idx][2] != -1:
        _inorder(tree, res, tree[idx][2])


def main():
    nodes = int(sys.stdin.readline().strip())
    if nodes == 0:
        print('CORRECT')
        return
    tree = []
    for i in range(nodes):
        tree.append(list(map(int, sys.stdin.readline().strip().split())))
    if IsBinarySearchTree(tree):
        print("CORRECT")
    else:
        print("INCORRECT")


threading.Thread(target=main).start()
