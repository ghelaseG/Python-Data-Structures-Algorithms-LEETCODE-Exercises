"""
You are given a doubly linked list.

Implement a method called swap_pairs within the class that swaps the values of adjacent nodes in the linked list. The method should not take any input parameters.

Note: This DoublyLinkedList does not have a tail pointer which will make the implementation easier.

Example:

1 <-> 2 <-> 3 <-> 4 should become 2 <-> 1 <-> 4 <-> 3

Your implementation should handle edge cases such as an empty linked list or a linked list with only one node.

Note: You must solve the problem WITHOUT MODIFYING THE VALUES in the list's nodes (i.e., only the nodes' prev and next pointers may be changed.)


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
        self.length = 1

    def print_list(self):
        output = []
        current_node = self.head
        while current_node is not None:
            output.append(str(current_node.value))
            current_node = current_node.value
        print("< - >".join(output))
    
    def append(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
        else:
            temp = self.head
            while temp.next is not None:
                temp = temp.next
            temp.next = new_node
            new_node.prev = temp
        self.length += 1
        return True
    



    def swap_pairs(self): 
        """ Let's take this example: LL: 1 <-> 2 <-> 3 <-> 4"""
        """
        Here we initialise a dummy node(starting at value 0), and
        we connect it to the LL, exp: 0 -> 1 <-> 2 <-> 3 <-> 4
        """
        dummy = Node(0)
        dummy.next = self.head #this simplifies the swapping process 
        """
        Previous pointer always points to the node just before the first node in the pair we're about to swap
        """
        previous = dummy
        """Let's check if we got at least 2 nodes in the LL"""
        while self.head is not None and self.head.next is not None:
            """Let's assign 2 nodes, to be swapped"""
            first_node = self.head
            second_node = self.head.next
            """previous node will point to the second node, exp: 0 -> 2,
               this should point to the second node of the pair after swapping"""
            previous.next = second_node
            """now we link through our first node(the end of our swapped pair) to the rest of the list,
               exp: 2 <-> 1 -> 3 <-> 4"""
            first_node.next = second_node.next
            """now we make the actual swap by reversing their next pointers, 
               exp: 2 <-> 1 -> 3 <-> 4"""
            second_node.next = first_node
            """let's update the previous pointers for a doubly ll,
               exp: """
            second_node.prev = previous
            first_node.prev = second_node
            
            if first_node.next is not None:
                first_node.next.prev = first_node
            self.head = first_node.next
            previous = first_node
            
        self.head = dummy.next
            
        if self.head is not None:
            self.head.prev = None

"""

LL: 1 <-> 2 <-> 3 <-> 4
Result: 2 <-> 1 <-> 4 <-> 3

"""