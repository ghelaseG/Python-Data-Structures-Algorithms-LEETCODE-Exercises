"""
Description

The merge method takes in another LinkedList as an input and merges it with the current LinkedList.

The elements in both lists are assumed to be in ascending order.

Parameters

other_list (LinkedList): the other LinkedList to merge with the current list



Return Value

This method does not return a value, but it modifies the current LinkedList to contain the merged list.



Example:

l1 = LinkedList(1)
l1.append(3)
l1.append(5)
l1.append(7)
 
l2 = LinkedList(2)
l2.append(4)
l2.append(6)
l2.append(8)
 
l1.merge(l2)
 
# The current list (l1) now contains the merged list [1, 2, 3, 4, 5, 6, 7, 8]


Detailed Steps:

Initialize Helper Nodes:

Create a "dummy" node that acts as a starting point, and give it a value of 0.

Create another node called "current" and set it to point to this dummy node. We'll use "current" to keep track of where we are in the new merged list.

Merge Loop:

This loop will go through each node in both the list we're working on (self.head) and the list we're merging into it (other_head).

For each pair of nodes (one from each list), compare their values.

Take the node with the smaller value and attach it to the "current" node.

Move both the "current" node and the list head that had the smaller value to their respective next nodes.

Check for Remaining Nodes:

After the loop, it's possible that one list still has nodes while the other doesn't.

If that's the case, take the remaining nodes from the list that isn't empty and attach them to "current".

Update Head, Tail, and Length:

Once you're done with the merging, the "dummy" node will still be at the start. Update the head of the list to point to the node that comes immediately after this dummy node.

Also, make sure to update the tail node to be the last node in the new, merged list.

Finally, update the length of the list to account for the nodes from both original lists.

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

    #this method is available only if both lists are sorted
    def merge(self, other_list):
        other_head = other_list.head
        dummy = Node(0) #we use this dummy node to hold the merged list
        current = dummy
        #loop while both lists have nodes
        while self.head is not None and other_head is not None:
            #compare the value of the first nodes in both lists
            if self.head.value < other_head.value:
                #in the first list, the smaller value is added to the current node
                ##and move to the next node
                current.next = self.head 
                self.head = self.head.next
            else:
                #for the second list, add the value and move to the next
                current.next = other_head
                other_head = other_head.next
            #move current node to the next position
            current = current.next
        
        #if the first list has any nodes left, add them to current
        if self.head is not None:
            current.next = self.head
        else:
            #if the second list has nodes left, add them to current
            current.next = other_head
            #update the tail of the merged list to be the tail of the second list
            self.tail = other_list.tail
        
        #set the head of the merged list to the next node after the dummy 
        self.head = dummy.next
        #update the length of the merged list
        self.length += other_list.length

l1 = LinkedList(1)
l1.append(3)
l1.append(5)
l1.append(7)

l2 = LinkedList(2)
l2.append(4)
l2.append(6)
l2.append(8)

l1.merge(l2)
l1.print_list()