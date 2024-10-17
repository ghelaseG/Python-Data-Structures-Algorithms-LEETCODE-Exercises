"""
Write a Python program to create a class representing a linked list data structure. Include methods for displaying linked list data, inserting and deleting nodes.
"""

class Node:

    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:

    def __init__(self):
        self.head = None

    #display the elements
    def display(self):
        current = self.head
        while current:
            print(current.data, end = "")
            current = current.next
        print()

    #insert a new node at the end of the linked list
    def insert(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node
        
    #delete a node with the given data
    def delete(self, data):
        if not self.head:
            return

        if self.head.data == data:
            self.head = self.head.next
            return
        
        current = self.head
        prev = None
        while current and current.data != data:
            prev = current
            current = current.next
        
        if current:
            prev.next = current.next


#examples
linked_list = LinkedList()

linked_list.insert(1)
linked_list.insert(2)
linked_list.insert(3)
linked_list.insert(4)

print("Initial linked list")
linked_list.display()

linked_list.insert(5)
print("After inserting a new node:")
linked_list.display()
