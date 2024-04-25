"""
The sort_stack function takes a single argument, a Stack object.  The function should sort the elements in the stack in ascending order (the lowest value will be at the top of the stack) using only one additional stack. 

The function should use the pop, push, peek, and is_empty methods of the Stack object.

Note: This is a new function, not a method within the Stack class. So, your indent should be all the way to the LEFT.
"""

class Stack:
    def __init__(self):
        self.stack_list = []

    def print_stack(self):
        for i in range(len(self.stack_list)-1, -1, -1):
            print(self.stack_list[i])
    
    def is_empty(self):
        return len(self.stack_list) == 0
    
    def peek(self):
        if self.is_empty():
            return None
        else:
            return self.stack_list[-1]
    
    def size(self):
        return len(self.stack_list) == 0
    
    def push(self, value):
        self.stack_list.append(value)

    def pop(self):
        if self.is_empty():
            return None
        else:
            return self.stack_list.pop()
        
def sort_stack(stack):
    sorted_stack = Stack()
    while not stack.is_empty:
        temp = stack.pop()
        
        while not sorted_stack.is_empty() and sorted_stack.peek() > temp:
            stack.push(sorted_stack.pop())
            
        sorted_stack.push(temp)
        
    while not sorted_stack.is_empty():
        stack.push(sorted_stack.pop())
        
