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

    def reverse(self):
        """
        - first way:
        #set the current node to head
        current = self.head
        
        while current is not None:
            temp_next = current.next

            current.next = current.prev
            current.prev = temp_next
            current = temp_next

        self.head, self.tail = self.tail, self.head"""

        temp = self.head
        while temp is not None:
            #swap the prev and next pointers,
            #this reverses the link direction for the node,
            #prev becomes next, and vice versa
            temp.prev, temp.next = temp.next, temp.prev

            #move to the next node
            #because we reverse the pointers, prev is actually next
            temp = temp.prev

            #swap the head and tail pointers
            self.head, self.tail = self.tail, self.head


my_doubly_linked_list = DoublyLinkedList(1)
my_doubly_linked_list.append(2)
my_doubly_linked_list.append(3)
my_doubly_linked_list.append(4)
my_doubly_linked_list.append(5)


print('DLL before reverse():')
my_doubly_linked_list.print_list()


my_doubly_linked_list.reverse()


print('\nDLL after reverse():')
my_doubly_linked_list.print_list()


