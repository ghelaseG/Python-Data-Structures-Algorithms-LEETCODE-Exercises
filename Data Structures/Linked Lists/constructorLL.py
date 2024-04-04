"""
Let's build the constructor for our Linked Lists

Let's see what each of this function does:

class LinkedList:
    def __init__(self, value):
    #create new Node 
    #initialise the class (or the new Linked Lists) - same as u do in git/github
    
    def append(self, value):
    #create new Node
    #add Node to end

    def prepend(self, value):
    #create new Node
    #add Node to beginning

    def insert(self, index, value):
    #create new Node
    #insert Node

    #instead of doing this tedious task, we can create a class that create Nodes.
    class Node:
        def __init__(self, value): #contains only this constructor
            self.value = value
            self.next = None
    
"""

class Node:
        def __init__(self, value): #contains only this constructor
            self.value = value
            self.next = None

class LinkedList:
      def __init__(self, value):
            new_node = Node(value)
            self.head = new_node
            self.tail = new_node
            self.length = 1

my_linked_list = LinkedList(4)

print(my_linked_list.head.value)