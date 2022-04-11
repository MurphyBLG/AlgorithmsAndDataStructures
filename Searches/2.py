from distutils.command.build import build
from lib2to3.pytree import Node
from logging import root


class Node:
    def __init__(self, value) -> None:
        self.value = value
        self.left = None
        self.right = None
        # self.parent = None


class BST:

    def __init__(self) -> None:
        self.root = None

    def build_tree(self, arr: list):
        if len(arr) == 0:
            return None

        mid = len(arr) // 2
        node = Node(arr[mid])

        if self.root == None:
            self.root = node

        node.left = self.build_tree(arr[:mid])
        node.right = self.build_tree(arr[mid + 1:])
        return node


if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    arr.sort()

    tree = BST()
    tree.build_tree(arr)


