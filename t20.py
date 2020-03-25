class Node:

    def __init__(self, data):
        self.left = 'left'
        self.right = 'right'
        self.data = data


# node = Node()

root = Node('tree')


class BinarySerachTree:
    def node_insert(self, root, data_to_find):
        while root != None:
            if data_to_find > root.data:
                if root.right is not None:
                    root = root.right
                else:
                    root.right = data_to_find
                    return root
            else:
                # data_to_find<root.data:
                if root.left is not None:
                    root = root.left
                else:
                    root.left = data_to_find
                    return root
