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

stack = Stack()

stack.push(10)
stack.push(20)
stack.push(30)
stack.push(40)
stack.push(50)

#display the items in the stack
stack.display()

#pop items from the stack and print the popped items
popped_item = stack.pop()
print("Popped item:", popped_item)

popped_item = stack.pop()
print("Popped item:", popped_item)

#display the updated stack
stack.display()