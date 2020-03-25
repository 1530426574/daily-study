class Node:

    def __init__(self, data):
        self.left = 'left'
        self.right = 'right'
        self.data = data


# node = Node()
tree = Node('root')
root = Node('tree')


class BinarySerachTree:
    def node_delete(self, root, data, tree):
        while root != None and root.data != data:
            pp = root
            if data > root.data:
                root = root.right
            else:
                root = root.left
        if root == None:
            return None
        if root.left != None and root.right != None:

            father = root
            child_right = root.right
            while child_right.left != None:
                father = child_right
                child_right = child_right.left
            root.data = child_right.data
            root = child_right
            pp = father

        if root.left is not None:
            pp.left = root.left

        if root.right == None:
            pp.right = root.right

        if root == tree:
            pass

    def add(self):
        pass

    def hello(self):
        pass
