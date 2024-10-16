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
        return len(self.items) == 0
    
    #get the number of items in the stack
    def size(self):
        return len(self.items)
    
    #peek at the top item of the stack without removing it, if the stack is not empty
    def peek(self):
        if not self.is_empty():
            return self.items[-1]
        else:
            return "Empty stack"
    
#example
stack = Stack()

#push items into the stack
stack.push(0)
stack.push(1)
stack.push(2)
stack.push(3)
stack.push(4)
stack.push(5)
    
print("Stack size:", stack.size())
print("Top element:", stack.peek())

# Pop an item from the stack, and print the popped item, and the updated size and top element
popped_item = stack.pop()
print("\nPopped item:", popped_item)
print("\nStack size:", stack.size())
print("Top element:", stack.peek())

# Create another instance of the Stack class
stack1 = Stack()

# Print the size of the empty stack and attempt to pop an item (with an error message)
print("\nStack size:", stack1.size())
popped_item = stack1.pop()
print("\nPopped item:", popped_item) 


