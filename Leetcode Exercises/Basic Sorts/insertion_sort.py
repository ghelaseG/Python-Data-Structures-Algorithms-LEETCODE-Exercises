"""
Assignment:

Write an insertion_sort() method in the LinkedList class that will sort the elements of a linked list in ascending order using the insertion sort algorithm.

The method should update the head and tail pointers of the linked list to reflect the new order of the nodes in the list.

You can assume that the input linked list will contain only integers. You should not use any additional data structures to sort the linked list.



Input:

The LinkedList object containing a linked list with unsorted elements (self).



Output:

None. The method sorts the linked list in place.



Method Description:

If the length of the linked list is less than 2, the method returns and the list is assumed to be already sorted.

The first element of the linked list is treated as the sorted part of the list, and the second element is treated as the unsorted part of the list.

The first element of the sorted part of the list is then disconnected from the rest of the list, creating a new linked list with only one element.

The method then iterates through each remaining node in the unsorted part of the list.

For each node in the unsorted part of the list, the method determines its correct position in the sorted part of the list by comparing its value with the values of the other nodes in the sorted part of the list.

Once the correct position has been found, the node is inserted into the sorted part of the list at the appropriate position.

After all the nodes in the unsorted part of the list have been inserted into the sorted part of the list, the head and tail pointers of the linked list are updated to reflect the new order of the nodes in the list.



Constraints:

The linked list can contain duplicates.

The method should be implemented in the LinkedList class.

The method should not use any additional data structures to sort the linked list.

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
            self.tail = new_node
        self.length += 1

    def insertion_sort(self):
        if self.length < 2:
            return
        
        sorted_list_head = self.head
        unsorted_list_head = self.head.next
        #here we disconnect this pointer from the rest of the list
        sorted_list_head.next = None
        
        #we iterate through the unsorted list
        while unsorted_list_head is not None:
            current= unsorted_list_head
            unsorted_list_head = unsorted_list_head.next
            #if the statement is true, current(unsorted_list_head) become the sorted_list_head node
            if current.value < sorted_list_head.value:
                current.next = sorted_list_head
                sorted_list_head = current
            else:
                #otherwise the function searches through the sorted part of the list
                ##to find the correct position to insert the current node
                search_pointer = sorted_list_head
                #the search is done using search_pointer, 
                ##the search pointer is moved until reaches the last node with a smaller value
                ###than the current node
                ####once that is found, current node is inserted in the sorted part of the list
                while search_pointer.next is not None and current.value > search_pointer.next.value:
                    search_pointer = search_pointer.next
                current.next = search_pointer.next
                search_pointer.next = current
        #in this last block of code, we update the head and tail attributes of the LL
        self.head = sorted_list_head
        temp = self.head
        while temp.next is not None:
            temp = temp.next
        self.tail = temp
        



my_linked_list = LinkedList(4)
my_linked_list.append(2)
my_linked_list.append(6)
my_linked_list.append(5)
my_linked_list.append(1)
my_linked_list.append(3)

print("Linked List Before Sort:")
my_linked_list.print_list()

my_linked_list.insertion_sort()

print("\nSorted linked list:")
my_linked_list.print_list()