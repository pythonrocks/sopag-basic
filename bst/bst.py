#            5
#          /   \
#         3     7
#       /  \   / \
#      1    2 6   9
#    search = O(log(n))


class Node:
    def __init__(self, val):
        self.val = val
        self.l = None
        self.r = None

    def __repr__(self):
        if self.val:
            return str(self.__dict__)
        else:
            return ''


# bst = Node(5)
# bst.l = Node(3)
# bst.r = Node(7)

# bst = {
#     5: {
#         3: {1: None, 2: None},
#         7: {6: None, 9: None}
#     }
# }


class BST:
    def __init__(self):
        self.root = None

    def insert(self, value):
        if self.root == None:
            self.root = Node(value)
        else:
            self._insert(self.root, value)

    def _insert(self, node, value):
        if value > node.val:
            if node.r is None:
                node.r = Node(value)
            else:
                self._insert(node.r, value)
        else:
            if node.l is None:
                node.l = Node(value)
            else:
                self._insert(node.l, value)


if __name__ == "__main__":
    bst = BST()
    bst.insert(5)
    bst.insert(7)
    bst.insert(3)
    bst.insert(1)
    bst.insert(2)
    bst.insert(6)
    bst.insert(9)
    print(bst.root)
