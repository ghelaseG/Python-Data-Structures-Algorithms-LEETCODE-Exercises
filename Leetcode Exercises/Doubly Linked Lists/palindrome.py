"""
Write a method to determine whether a given doubly linked list reads the same forwards and backwards.

For example, if the list contains the values [1, 2, 3, 2, 1], then the method should return True, since the list is a palindrome.

If the list contains the values [1, 2, 3, 4, 5], then the method should return False, since the list is not a palindrome.
"""

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None
    
class DoublyLinkedList:
    def __init__(self, value):
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node
        self.length = 1

    def print_list(self):
        temp = self.head
        while temp is not None:
            print(temp.value)
            temp = temp.next

    def append(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node
        self.length += 1
        return True
    
    def is_palindrome(self):
        # if the length of the list have only 1 number, then by definition it is a palindrome
        if self.length <= 1:
            return True
        
        #we initialise 2 pointers, first and last node
        forward_node = self.head
        backward_node = self.tail
        #as we compare the first with the last, the for loop iterates only half of the LL
        for _ in range(self.length // 2):
            #if those values are different, we exit, as the list is not a palindrome, otherwise, it will return true
            if forward_node.value != backward_node.value:
                return False
        #here it will move one step forwerd, and backwards, then the loop it will start again, until we reach the half of it
        forward_node = forward_node.next
        backward_node = backward_node.prev
        return True