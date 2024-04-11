class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self, value):
        new_node = Node(value)
        self.head = new_node
        self.length = 1

    def append(self, value):
        new_node = Node(value)
        if self.length == 0:
            self.head = new_node
        else:
            current_node = self.head
            while current_node.next is not None:
                current_node = current_node.next
            current_node.next = new_node
        self.length += 1

    def print_list(self):
        temp = self.head
        while temp is not None:
            print(temp.value)

    def make_empty(self):
        self.head = None
        self.tail = None
        self.length = 0

    def partition_list(self, x):
        #check if the list is empty
        if self.length == 0:
            return None
        #initialize dummy1 and dummy2 as new nodes with value 0
        dummy1 = Node(0)
        dummy2 = Node(0)
        #the two pointers prev1 and prev2, will be used to
        #build two separate lists
        prev1 = dummy1
        prev2 = dummy2
        #using ""current" pointer, we can iterate through the
        #linked lists, starting of course at the first node
        current = self.head
        #now we check if the current is not null, the the value the
        #he is getting, if it is smaller than the value of x, then we 
        #add it to the prev1 pointer, otherwise to the other one
        while current is not None:
            if current.value < x:
                prev1.next = current
                prev1 = current
            else:
                prev2.next = current
                prev2 = current
            #here we use this so the while loop helps current to go
            #to the next node
            current = current.next
        #now we link the first list with the second list
        prev1.next = dummy2.next
        #here we end the second list
        prev2.next = None
        #then we make sure that the head of the linked list point to 
        #the beginning of the partitioned list
        dummy1.next = self.head
        