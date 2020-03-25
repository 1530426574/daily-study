class Node:

    def __init__(self, data):
        self.left = 'left'
        self.right = 'right'
        self.data = data


# node = Node()

root = Node('tree')


class BinarySerachTree:
    def node_find(self, root, data_to_find):
        while root != None:
            if data_to_find < root.data:
                root = root.left
            elif data_to_find > root.data:
                root = root.right
            else:
                return root
