class Node:
    def __init__(self, value=None):
        self.value = value
        self.left = None
        self.right = None
        self.depth = None
        
        
    def insert(self, value):
        if self.value is None:
            self.value = value
        elif value < self.value:
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
    def in_order_traversal(tree):
        ordered_elements=[]
        if tree:
            ordered_elements = Node.in_order_traversal(tree.left)
            ordered_elements.append(tree.value)
            ordered_elements.extend(Node.in_order_traversal(tree.right))
        return ordered_elements

    @staticmethod
    def max_depth(tree, depth = 0):
        if tree is None:
            return depth - 1 

        left_depth = Node.max_depth(tree.left,depth+1)
        right_depth = Node.max_depth(tree.right,depth+1)
        return max(left_depth, right_depth)
    
    @staticmethod
    def contains(tree, value):
        if tree is None:
            return False
        if tree.value == value:
            return True
        if value < tree.value:
            return Node.contains(tree.left, value)
        else:
            return Node.contains(tree.right, value)
            
        return False



# tree = Node()

# tree.insert(1)
# tree.insert(2)
# tree.insert(3)
# tree.insert(4)
# tree.insert(5)
# tree.insert(6)
# tree.insert(7)

# assert tree.in_order_traversal(tree) == [1, 2, 3, 4, 5, 6, 7]
# assert tree.contains(tree, 3)
# assert not tree.contains(tree, 20)
# assert tree.max_depth(tree) <= 6

# print(tree.max_depth(tree))


tree = Node()

tree.insert(2)
tree.insert(10)
tree.insert(3)
tree.insert(5)
tree.insert(100)

assert tree.max_depth(tree) <= 2
print(tree.max_depth(tree))







# Another TEST CASE
#  Create the tree node
# tree = Node(7)

# # Insert some nodes into the tree
# tree.insert(5)
# tree.insert(15)
# tree.insert(3)
# tree.insert(7)
# tree.insert(12)
# tree.insert(20)


# # Print the tree
# Node.print_tree(tree)

# # Get the values in the tree in in-order traversal order
# values = []
# Node.in_order_traversal(tree, values)
# print(values)

# # Get the maximum depth of the tree
# print(Node.max_depth(tree))

# # Check if the tree contains a particular value
# print(Node.contains(tree, 7))
# print(Node)




    # def insert(self, value):
    #     if value < self.value:
    #         if self.left is None:
    #             self.left = Node(value)
    #         else:
    #             self.left.insert(value)
    #     else:
    #         if self.right is None:
    #             self.right = Node(value)
    #         else:
    #             self.right.insert(value)