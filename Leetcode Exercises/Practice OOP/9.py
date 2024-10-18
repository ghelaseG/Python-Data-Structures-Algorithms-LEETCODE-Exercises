"""
Write a Python program to create a class representing a stack data structure. Include methods for pushing, popping and displaying elements.
"""

class Stack:
    #initialise an empty list
    def __init__(self):
        self.items = []

    def push(self, item):
        return self.items.append(item)
    
    def pop(self):
        if not self.is_empty():
            return self.items.pop()
        else:
            raise IndexError("Cannot pop from an empty stack.")
        
    def is_empty(self):
        return len(self.items) == 0
    
    def display(self):
        print("Stack Items", self.items)