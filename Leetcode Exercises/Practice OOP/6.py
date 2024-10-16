"""
Write a Python program to create a class representing a stack data structure. Include methods for pushing and popping elements.
"""

class Stack:
    #initialise the stack with an empty list to store the items
    def __init__(self):
        self.items = []

    #push item into the stack
    def push(self, item):
        self.items.append(item)

    #remove and return an item from the stack if the stack is not empty
    def pop(self):
        if not self.is_empty():
            return self.items.pop()
        else:
            return "Cannot pop from empty list"
    
    #check if the stack is empty
    def is_empty(self):
        
