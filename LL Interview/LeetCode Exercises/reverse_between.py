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
    
    def make_empty(self):
        self.head = None
        self.length = 0

    def reverse_between(self, start_index, end_index):
        if self.length <= 1 or start_index >= end_index:
            return None
        
        previous_node = None
        current_node = self.head
        count = 1

        while current_node and count < start_index:
            previous_node = current_node
            current_node = current_node.next
            count += 1

        first_node = previous_node
        last_node = current_node

        while current_node and count <= end_index:
            next_node = current_node.next
            current_node.next = previous_node
            previous_node = current_node
            current_node = next_node
            count += 1

        if first_node is not None:
            first_node.next = previous_node
        else:
            self.head = previous_node

        last_node.next = current_node
        
linked_list = LinkedList(1)
linked_list.append(2)
linked_list.append(3)
linked_list.append(4)
linked_list.append(5)

print("Original linked list: ")
linked_list.print_list()

# Reverse a sublist within the linked list
linked_list.reverse_between(2, 4)
print("Reversed sublist (2, 4): ")
linked_list.print_list()

# Reverse another sublist within the linked list
linked_list.reverse_between(0, 4)
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
empty_list.print_list()