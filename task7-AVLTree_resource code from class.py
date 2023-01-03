class Node:
    def __init__(self, data=None):
        self.data = data
        self.left = None
        self.right = None
        self.depth = None

    
    def insert(self, data):
    
        if self.data: # check if root exists
            if data < self.data: # are new data smaller?
                if self.left is None: # is left reference free?
                    self.left = Node(data) # put data into free left reference
                else:
                    self.left.insert(data) # otherwise call the function again
            elif data > self.data: # the same for right subtree
                if self.right is None:
                    self.right = Node(data)
                else:
                    self.right.insert(data)
        else:
            self.data = data # if root has no data, insert data into the root
            
    #we can use static method for recursion because we could not do it with "self" object.
    #otherwise we should write: def print_tree(self, tree, level=0, prefix=""):
    #and use the tree object as a helper object.
    @staticmethod
    def print_tree(tree, level=0, prefix=""):
        if tree.data: # check if tree root has data
            # print a space proportional to the depth level of a tree
            print(" "*(4*level) + prefix + str(tree.data))
            if tree.left:
                 # call the function for left subtrees and increment the depth level.
                 # prefix is "L: " which means left.
                Node.print_tree(tree.left,level=level+1,prefix="L:")
            if tree.right:
                 # call the function for rught subtrees and increment the depth level
                Node.print_tree(tree.right,level=level+1,prefix="R:")

    
    @staticmethod            
    def in_order_traversal(tree):
        ordered_elements = [] # prepare empty list
        if tree:
            ordered_elements = Node.in_order_traversal(tree.left)
            ordered_elements.append(tree.data)
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
    def contains(tree, data):
        if tree: 
            if tree.data == data: # if the data equals to subroot return True
                return True
            if tree.data > data:
                # if the data are bigger than the value of subroot, call the recursion with left subtree
                return Node.contains(tree.left, data)
            else:
                 # if the data are smaller than the value of subroot, call the recursion with right subtree
                return Node.contains(tree.right, data)
        return False # if no match is found, return false
        
tree = Node()

tree.insert(1)
tree.insert(2)
tree.insert(3)
tree.insert(4)
tree.insert(5)
tree.insert(6)
tree.insert(7)

assert tree.in_order_traversal(tree) == [1, 2, 3, 4, 5, 6, 7]
assert tree.contains(tree, 3)
assert not tree.contains(tree, 20)
assert tree.max_depth(tree) <= 2


# tree = Node()

# tree.insert(2)
# tree.insert(10)
# tree.insert(3)
# tree.insert(5)
# tree.insert(100)

# assert tree.max_depth(tree) <= 2        

# bin_tree = Node()

# bin_tree.insert(10)
# bin_tree.insert(5)
# bin_tree.insert(3)
# bin_tree.insert(20)
# bin_tree.insert(200)
# bin_tree.insert(40)
# bin_tree.insert(300)
# bin_tree.insert(30)



# bin_tree.print_tree(bin_tree)
# print(bin_tree.contains(bin_tree,19))
        
