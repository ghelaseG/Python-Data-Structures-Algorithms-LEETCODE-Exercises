class Node:
    def __init__(self, value):
        self.value = value
        self.next = next

class Stack:
    def __init__(self, value):
        new_node = Node(value)
        self.top = new_node
        self.height = 1

    def push(self, value):
        new_node = Node(value)
        if self.height == 0:
            self.top = new_node
        else:
            new_node.next = self.top
            self.top = new_node
        self.height += 1

my_stack = Stack(2)
my_stack.push(1)

my_stack.print_stack()