class Node(object):
    def __init__(self, data=None, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right


class BinarySearchTree(object):
    def __init__(self, root=None):
        self.root = root

    def get_root(self):
        return self.root

    def insert(self, item):
        if self.root is None:
            self.root = Node(item)
        else:
            cur_node = self.root
            while cur_node is not None:
                if item < cur_node.data:
                    if cur_node.left is None:
                        cur_node = Node(item)
                        return
                    else:
                        cur_node = cur_node.left
                else:
                    if cur_node.right is None:
                        cur_node = Node(item)
                        return
                    else:
                        cur_node = cur_node.right
