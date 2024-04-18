"""
Write a method called has_loop that is part of the linked list class.

The method should be able to detect if there is a cycle or loop present in the linked list.

You are required to use Floyd's cycle-finding algorithm (also known as the "tortoise and the hare" algorithm) to detect the loop.

This algorithm uses two pointers: a slow pointer and a fast pointer. The slow pointer moves one step at a time, while the fast pointer moves two steps at a time. If there is a loop in the linked list, the two pointers will eventually meet at some point. If there is no loop, the fast pointer will reach the end of the list.

The method should follow these guidelines:



Create two pointers, slow and fast, both initially pointing to the head of the linked list.

Traverse the list with the slow pointer moving one step at a time, while the fast pointer moves two steps at a time.

If there is a loop in the list, the fast pointer will eventually meet the slow pointer. If this occurs, the method should return True.

If the fast pointer reaches the end of the list or encounters a None value, it means there is no loop in the list. In this case, the method should return False.

"""

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self, value):
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node
        self.length = 1

    def append(self, value):
        new_node = Node(value)
        if self.length == 0:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        self.length += 1
        return True
    
    def has_loop(self): # we are using Floyd's cycle-finding algorithm
        slow_pointer = self.head #tortoise
        fast_pointer = self.head #the hare
        while fast_pointer is not None and fast_pointer.next is not None: # we check to make sure are values, minimum 2 values/nodes
            slow_pointer = slow_pointer.next #tortoise
            fast_pointer = fast_pointer.next.next #the hare

            if slow_pointer == fast_pointer: # if the tortoise and the hare are meeting, then the linked list has a loop (cycle)
                return True
            
        return False # otherwise it does not have
    
my_linked_list = LinkedList(1)
my_linked_list.append(2)
my_linked_list.append(3)
my_linked_list.append(4)
my_linked_list.append(5)
my_linked_list.tail.next = my_linked_list.head #here we add the head node to the tail node
print(my_linked_list.has_loop()) #indeed it returns True because of my_linked_list.tail.next = my_linked_list.head