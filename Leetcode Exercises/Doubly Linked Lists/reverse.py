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
        self.length +=1
    
    def print_list(self):
        temp = self.head
        while temp is not None:
            print(temp.value)
            temp = temp.next

    def append(self, value):
        new_node = Node(0)
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
        if self.length == 0:
            return None
        
        dummy = Node(0)
        dummy.next = self.head
        previous_node = dummy.prev

        for _ in range(self.length):
            previous_node = previous_node.next
            after = previous_node.next

            new_node.prev = previous_node
            new_node.next = after
            previous_node.next = new_node
            after.prev = new_node

            self.head = dummy
            self.tail = previous_node

