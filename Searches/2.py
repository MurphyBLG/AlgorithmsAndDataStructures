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


    def find(self, key: int):
        cur = self.root

        while cur.left != None and cur.right != None and cur.value != key:
            if cur.value > key:
                cur = cur.left
            
            if cur.value < key:
                cur = cur.right

        if cur.value == key:
            return cur
        else:
            return None


    def find_min(self, node: Node):
        cur = node
        while cur.left != None:
            cur = cur.left

        return cur


    def delete(self, node: Node, value: int):
        if node is None:
            return node
    
        if value < node.value:
            node.left = self.delete(node.left, value)
        elif value > node.value:
            node.right = self.delete(node.right, value)
        else:
            if node.left is None:
                temp = node.right
                node = None
                return temp
            elif node.right is None:
                temp = node.left
                node = None
                return temp
    
            temp = self.find_min(node.right)
            node.value = temp.value
            node.right = self.delete(node.right, temp.value)
    
        return node


    def printTree(self, node, level=0):
        if node != None:
            self.printTree(node.left, level + 1)
            print(' ' * 4 * level + '-> ' + str(node.value))
            self.printTree(node.right, level + 1)



if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    arr.sort()

    tree = BST()
    tree.build_tree(arr)

    print(tree.find(5))
    tree.printTree(node=tree.root)
    tree.delete(node=tree.root, value=6)
    tree.printTree(node=tree.root)

