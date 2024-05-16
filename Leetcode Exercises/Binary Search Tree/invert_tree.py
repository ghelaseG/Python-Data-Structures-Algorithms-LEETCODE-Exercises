"""
Objective: Write a method to invert (or mirror) a binary tree. This means that for every node in the binary tree, you will swap its left and right children.

Requirements:

The method must be recursive. It should work by traversing the tree and swapping the left and right children of every node encountered.

If the input tree is empty (i.e., node is None), the method should return None.

The inversion should happen in-place, meaning you should not create a new tree but instead modify the existing tree structure.

The method should handle binary trees of any size and structure, ensuring that every node's left and right children are swapped.

Note: This problem requires understanding binary trees, recursion, and the ability to manipulate tree nodes directly. The solution should ensure that every node's left and right children are swapped all the way down the tree, effectively creating a mirror image of the original structure.
"""

def __invert_tree(self, node):
    if not node:
        return None
    
    temp = self.left
    self.left = self.right
    self.right = temp

    self.__invert_tree(self.left)
    self.__invert_tree(self.right)
    return node