"""
Implement the find_kth_from_end function, which takes the LinkedList (ll) and an integer k as input, and returns the k-th node from the end of the linked list WITHOUT USING LENGTH.

Given this LinkedList:

1 -> 2 -> 3 -> 4

If k=1 then return the first node from the end (the last node) which contains the value of 4.

If k=2 then return the second node from the end which contains the value of 3, etc.

If the index is out of bounds, the program should return None.

The find_kth_from_end function should follow these requirements:

The function should utilize two pointers, slow and fast, initialized to the head of the linked list.

The fast pointer should move k nodes ahead in the list.

If the fast pointer becomes None before moving k nodes, the function should return None, as the list is shorter than k nodes.

The slow and fast pointers should then move forward in the list at the same time until the fast pointer reaches the end of the list.

The function should return the slow pointer, which will be at the k-th position from the end of the list.



This is a separate function that is not a method within the LinkedList class. This means you need to indent the function all the way to the LEFT. 
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

        
    def append(self, value):
        new_node = Node(value)
        if self.head == None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        return True
  
  
def find_kth_from_end(self, k):
    #here we make sure the pointer starts from the first node, or better said it gets that value
    slow_pointer = self.head
    fast_pointer = self.head
    #now we iterate through the linked list k times
    #(for exp k=3, so fast pointer will go to the third index), 
    #unless the linked list is empty then it will return none
    for _ in range(k):
        if fast_pointer is None: 
            return None 
        fast_pointer = fast_pointer.next
    #here we iterate until one of the pointer(which of course will be the fast one)
    #reaches the Node with the null value, tail.next or next value after the tail    
    while fast_pointer is not None: #in case node is not empty
        slow_pointer = slow_pointer.next
        fast_pointer = fast_pointer.next 
    #when the fast_pointer has reached, for example:
    #k=3, the hare - started at 4, while the tortoise started at 1 (this was in the for loop)
    #using the while loop, let's say our linked list has got 6 values
    # 1->2->3->4->5->6 - this will mean that the tortoise 1, the hare 4,
    # once it advances, and the hare reaches 6, the tortoise it will be at 3, which is incorrect becase we need the kth node from the end
    #but it is not finished, meaning that the hare has to go one more step forward, to reach null - once this happens then the tortoise reach number 4
    return slow_pointer



my_linked_list = LinkedList(1)
my_linked_list.append(2)
my_linked_list.append(3)
my_linked_list.append(4)
my_linked_list.append(5)


k = 2
result = find_kth_from_end(my_linked_list, k)

print(result.value)  # Output: 4



"""
    EXPECTED OUTPUT:
    ----------------
    4
    
"""

