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
    #here we create a new stack to hold the sorted elements
    new_stack = Stack()
    #if the original stack is not empty, we remove the top element
    while not stack.is_empty():
        temp = stack.pop()
        #if the new stack is not empty and the top element is greater than the current element stored in temp
        while not new_stack.is_empty() and new_stack.peek() > temp:
            #we move the top element from the new stack to the original stack
            stack.push(new_stack.pop())
        #now we add the current element(from temp) to the new stack   
        new_stack.push(temp)
    #we then copy the sorted elements from the new stack to the original stack    
    while not new_stack.is_empty():
        stack.push(new_stack.pop())
        

my_stack = Stack()
my_stack.push(3)
my_stack.push(1)
my_stack.push(5)
my_stack.push(4)
my_stack.push(2)

print("Stack before sort_stack():")
my_stack.print_stack()

sort_stack(my_stack)

print("\nStack after sort_stack:")
my_stack.print_stack()