class Node:
    def __init__(self, value=None):
        self.value = value
        self.left = None
        self.right = None

    def insert(self, value):
        if value < self.value:
            if self.left is None:
                self.left = Node(value)
            else:
                self.left.insert(value)
        else:
            if self.right is None:
                self.right = Node(value)
            else:
                self.right.insert(value)

    @staticmethod
    def print_tree(tree, indent=''):
        if tree is not None:
            Node.print_tree(tree.right, indent + '    ')
            print(indent + str(tree.value))
            Node.print_tree(tree.left, indent + '    ')

    @staticmethod
    def in_order_traversal(tree, values):
        if tree is not None:
            Node.in_order_traversal(tree.left, values)
            values.append(tree.value)
            Node.in_order_traversal(tree.right, values)

    @staticmethod
    def max_depth(tree):
        if tree is None:
            return 0
        left_depth = Node.max_depth(tree.left)
        right_depth = Node.max_depth(tree.right)
        return max(left_depth, right_depth) + 1

    @staticmethod
    def contains(tree, data):
        if tree is None:
            return False
        if tree.value == data:
            return True
        if data < tree.value:
            return Node.contains(tree.left, data)
        else:
            return Node.contains(tree.right, data)



tree = Node(7)

tree.insert(1)
tree.insert(2)
tree.insert(3)
tree.insert(4)
tree.insert(5)
tree.insert(6)
tree.insert(7)

assert tree.in_order_traversal(tree) == [1, 2, 3, 4, 5, 6, 7]

# Another TEST CASE
#  # Create the root node
# root = Node(10)

# # Insert some nodes into the tree
# root.insert(5)
# root.insert(15)
# root.insert(3)
# root.insert(7)
# root.insert(12)
# root.insert(20)


# # Print the tree
# Node.print_tree(root)

# # Get the values in the tree in in-order traversal order
# values = []
# Node.in_order_traversal(root, values)
# print(values)

# # Get the maximum depth of the tree
# print(Node.max_depth(root))

# # Check if the tree contains a particular value
# print(Node.contains(root, 7))
# print(Node)

