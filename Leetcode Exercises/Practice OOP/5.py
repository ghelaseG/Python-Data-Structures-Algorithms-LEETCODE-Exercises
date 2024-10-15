"""
Write a Python program to create a class representing a binary search tree. Include methods for inserting and searching for elements in the binary tree.
"""

"""
Binary search tree:

In computer science, a binary search tree (BST), also called an ordered or sorted binary tree, is a rooted binary tree data structure with the key of each internal node being greater than all the keys in the respective node's left subtree and less than the ones in its right subtree. The time complexity of operations on the binary search tree is directly proportional to the height of the tree.
"""

class Node:
    #initialise the Node object with a value
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    #define a custome str method to convert the nodes value to a string
    def __str__(self):
        return str(self.value)
    
class BinarySearchTree:
    #initialise with an empty root node
    def __init__(self):
        self.root = None
    
    #insert value into the BST
    def insert(self, value):
        #if the root is None, create a new node with the given value as the root
        if self.root is None:
            self.root = Node(value)
        else:
            self._insert_recursive(self.root, value)

    #helper method to recursively insert a value into the BST
    def _insert_recursive(self, node, value):
        if value < node.value:
            if node.left is None:
                node.left = Node(value)
            else:
                self._insert_recursive(node.left, value)
        
        elif value > node.value:
            if node.right is None:
                node.right = Node(value)
            else:
                self._insert_recursive(node.right, value)

    #search for a value in the BST
    def search(self, value):
        return self._search_recursive(self.root, value)
    
    #helper method to recursively search for a value in the BST and return the node if found
    def _search_recursive(self, node, value):
        if node is None or node.value == value:
            return node
        if value < node.value:
            return self._search_recursive(node.left, value)
        else:
            return self._search_recursive(node.right, value)
        
bst = BinarySearchTree()

#insert values into the BST

bst.insert(5)
bst.insert(3)
bst.insert(7)
bst.insert(2)
bst.insert(4)
bst.insert(6)
bst.insert(8)

print("Searching for elements:")
print(bst.search(4))  
print(bst.search(9))  
    