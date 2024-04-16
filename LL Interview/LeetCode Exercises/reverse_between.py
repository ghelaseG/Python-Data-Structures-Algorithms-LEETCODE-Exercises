"""
⚠️ Advanced Challenge Alert: Linked List Mastery!
Welcome to what many consider the pinnacle of Linked List challenges in this course! This exercise is not just a test of your coding skills, but also a measure of your problem-solving ability and understanding of complex data structures.

Here's how you can tackle it:

Visualize the Problem: Before diving into coding, grab a pen and paper. Sketch out the linked list and visualize each step of the process. This approach isn't just for beginners; it's exactly how seasoned developers plan their attack on complex problems.

Seek Understanding Over Speed: Take your time to really grasp each part of the problem. The goal here is deep understanding, not just a quick solution. If you find yourself stuck, that's a part of the learning process.

It's Okay to Take a Break: Feel free to step away from this challenge and return later. This course is designed to equip you with a growing set of skills, and sometimes, a bit of distance can bring new insights.

Approach Like a Pro: Remember, facing a challenging problem is what being a professional developer is all about. Use this exercise to think, plan, and code like a pro.


"""

"""
You are given a singly linked list and two integers start_index and end_index.

Your task is to write a method reverse_between within the LinkedList class that reverses the nodes of the linked list from start_index to  end_index (inclusive using 0-based indexing) in one pass and in-place.

Note: the Linked List does not have a tail which will make the implementation easier.

Assumption: You can assume that start_index and end_index are not out of bounds.



Input

The method reverse_between takes two integer inputs start_index and end_index.

The method will only be passed valid indexes (you do not need to test whether the indexes are out of bounds)



Output

The method should modify the linked list in-place by reversing the nodes from start_index to  end_index.

If the linked list is empty or has only one node, the method should return None.
"""

# Constraints
## The algorithm should run in one pass and in-place, with a time complexity of O(n) and a space complexity of O(1).

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
            current = self.head
            while current.next is not None:
                current = current.next
            current.next = new_node
        self.length += 1
        return True
    
    def print_list(self):
        temp = self.head
        while temp is not None:
            print(temp.value)
            temp = temp.next

    def make_empty(self):
        self.head = None
        self.length = 0

    def reverse_between(self, start_index, end_index):
        # let's first check if the linked list is empty
        if self.length <= 1:
            return None
        """let's take an example: start index = 2 | end index = 4, where our list is 1 -> 2 -> 3 -> 4 -> 5 -> 6"""
        #now we create a dummy variable
        ##in this variable, we can store our reversed sublist or reversed linked list, upon request
        ###also helps simplifying our code
        """dummy will be out of range, Null or just before node: (here) 1 ->"""
        dummy = Node(0)
        #we point our dummy node to the head of the list
        """now it will point to the first node(head): dummy -> 1"""
        dummy.next = self.head
        #we give the previous node our dummy values
        """previous will be null too, just here"""
        previous_node = dummy
        #here we iterate until we reach the index before start_index
        """now this will become, depending on our start index, and ours is 2, so it will iterate 2 times,
           meaning that previous_node will point at index(1), node 2 - because we start counting from zero"""
        for _ in range(start_index):
            """this will point at 2 ->"""
            previous_node = previous_node.next 
        # current will point to the node where the sublist starts to reverse
        """current will point at index(2), node 3, where our reversal starts -> 3 -> 4 etc"""
        current = previous_node.next
        """our first iteration, reversing node at index 3, node 4
           node_to_move will point to index 3, node 4 ( as current was index 2 node 3)
           current.next(index2, node3) will point to index 4 node 5
           node_to_move(index3, node4) will point to index 2 node 3
           previous_node(index1, node2) will point to index 3, node 4
           this will give us: 1 -> 2 -> 4 -> 3 -> 5 -> 6"""
        
        """second iteration, reversing at index 4, node 5
           node_to_move will next point to index 4, node 5
           current.next(index2, node3) will point to index 5, node 6
           node_to_move(index4, node5) will point to index 3, node 4
           previous_node(index1, node 2) will point to index 4, node 5
           we get: 1 -> 2 -> 5 -> 4 -> 3 -> 6"""
        for _ in range(end_index - start_index):
            node_to_move = current.next
            current.next = node_to_move.next
            node_to_move.next = previous_node.next
            previous_node.next = node_to_move

        self.head = dummy.next

linked_list = LinkedList(1)
linked_list.append(2)
linked_list.append(3)
linked_list.append(4)
linked_list.append(5)
linked_list.append(6)

print("Original linked list: ")
linked_list.print_list()

# Reverse a sublist within the linked list
linked_list.reverse_between(2, 4)
print("Reversed sublist (2, 4): ")
linked_list.print_list()

# Reverse another sublist within the linked list
'''linked_list.reverse_between(0, 4)
print("Reversed entire linked list: ")
linked_list.print_list()

# Reverse a sublist of length 1 within the linked list
linked_list.reverse_between(3, 3)
print("Reversed sublist of length 1 (3, 3): ")
linked_list.print_list()

# Reverse an empty linked list
empty_list = LinkedList(0)
empty_list.make_empty()
empty_list.reverse_between(0, 0)
print("Reversed empty linked list: ")
empty_list.print_list()'''