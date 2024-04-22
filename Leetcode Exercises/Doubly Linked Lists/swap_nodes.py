"""
You are given a doubly linked list.

Implement a method called swap_pairs within the class that swaps the values of adjacent nodes in the linked list. The method should not take any input parameters.

Note: This DoublyLinkedList does not have a tail pointer which will make the implementation easier.

Example:

1 <-> 2 <-> 3 <-> 4 should become 2 <-> 1 <-> 4 <-> 3

Your implementation should handle edge cases such as an empty linked list or a linked list with only one node.

Note: You must solve the problem WITHOUT MODIFYING THE VALUES in the list's nodes (i.e., only the nodes' prev and next pointers may be changed.)


"""

# for a better understanding, please use this link: 
# https://pythontutor.com/render.html#code=class%20Node%3A%0A%20%20%20%20def%20__init__%28self,%20value%29%3A%0A%20%20%20%20%20%20%20%20self.value%20%3D%20value%0A%20%20%20%20%20%20%20%20self.next%20%3D%20None%0A%20%20%20%20%20%20%20%20self.prev%20%3D%20None%0A%20%20%20%20%20%20%20%20%0A%0Aclass%20DoublyLinkedList%3A%0A%20%20%20%20def%20__init__%28self,%20value%29%3A%0A%20%20%20%20%20%20%20%20new_node%20%3D%20Node%28value%29%0A%20%20%20%20%20%20%20%20self.head%20%3D%20new_node%0A%20%20%20%20%20%20%20%20self.length%20%3D%201%0A%0A%20%20%20%20def%20print_list%28self%29%3A%0A%20%20%20%20%20%20%20%20output%20%3D%20%5B%5D%0A%20%20%20%20%20%20%20%20current_node%20%3D%20self.head%0A%20%20%20%20%20%20%20%20while%20current_node%20is%20not%20None%3A%0A%20%20%20%20%20%20%20%20%20%20%20%20output.append%28str%28current_node.value%29%29%0A%20%20%20%20%20%20%20%20%20%20%20%20current_node%20%3D%20current_node.next%0A%20%20%20%20%20%20%20%20print%28%22%20%3C-%3E%20%22.join%28output%29%29%0A%20%20%20%20%20%20%20%20%0A%20%20%20%20def%20append%28self,%20value%29%3A%0A%20%20%20%20%20%20%20%20new_node%20%3D%20Node%28value%29%0A%20%20%20%20%20%20%20%20if%20self.head%20is%20None%3A%0A%20%20%20%20%20%20%20%20%20%20%20%20self.head%20%3D%20new_node%0A%20%20%20%20%20%20%20%20else%3A%0A%20%20%20%20%20%20%20%20%20%20%20%20temp%20%3D%20self.head%0A%20%20%20%20%20%20%20%20%20%20%20%20while%20temp.next%20is%20not%20None%3A%0A%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20temp%20%3D%20temp.next%0A%20%20%20%20%20%20%20%20%20%20%20%20temp.next%20%3D%20new_node%0A%20%20%20%20%20%20%20%20%20%20%20%20new_node.prev%20%3D%20temp%0A%20%20%20%20%20%20%20%20self.length%20%2B%3D%201%0A%20%20%20%20%20%20%20%20return%20True%0A%0A%20%20%20%20def%20swap_pairs%28self%29%3A%0A%20%20%20%20%20%20%20%20dummy%20%3D%20Node%280%29%0A%20%20%20%20%20%20%20%20dummy.next%20%3D%20self.head%0A%0A%20%20%20%20%20%20%20%20previous%20%3D%20dummy%0A%0A%20%20%20%20%20%20%20%20while%20self.head%20is%20not%20None%20and%20self.head.next%20is%20not%20None%3A%0A%20%20%20%20%20%20%20%20%20%20%20%20first_node%20%3D%20self.head%0A%20%20%20%20%20%20%20%20%20%20%20%20second_node%20%3D%20self.head.next%0A%20%20%20%20%20%20%20%20%20%20%20%20previous.next%20%3D%20second_node%0A%20%20%20%20%20%20%20%20%20%20%20%20first_node.next%20%3D%20second_node.next%0A%20%20%20%20%20%20%20%20%20%20%20%20second_node.next%20%3D%20first_node%0A%20%20%20%20%20%20%20%20%20%20%20%20second_node.prev%20%3D%20previous%0A%20%20%20%20%20%20%20%20%20%20%20%20first_node.prev%20%3D%20second_node%0A%20%20%20%20%20%20%20%20%20%20%20%20%0A%20%20%20%20%20%20%20%20%20%20%20%20if%20first_node.next%20is%20not%20None%3A%0A%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20first_node.next.prev%20%3D%20first_node%0A%20%20%20%20%20%20%20%20%20%20%20%20self.head%20%3D%20first_node.next%0A%20%20%20%20%20%20%20%20%20%20%20%20previous%20%3D%20first_node%0A%20%20%20%20%20%20%20%20%20%20%20%20%0A%20%20%20%20%20%20%20%20self.head%20%3D%20dummy.next%0A%20%20%20%20%20%20%20%20%20%20%20%20%0A%20%20%20%20%20%20%20%20if%20self.head%20is%20not%20None%3A%0A%20%20%20%20%20%20%20%20%20%20%20%20self.head.prev%20%3D%20None%0A%0A%0A%0Amy_dll%20%3D%20DoublyLinkedList%281%29%0Amy_dll.append%282%29%0Amy_dll.append%283%29%0Amy_dll.append%284%29%0A%0Aprint%28'my_dll%20before%20swap_pairs%3A'%29%0Amy_dll.print_list%28%29%0A%0Amy_dll.swap_pairs%28%29%20%0A%0A%0Aprint%28'my_dll%20after%20swap_pairs%3A'%29%0Amy_dll.print_list%28%29&cumulative=false&curInstr=104&heapPrimitives=nevernest&mode=display&origin=opt-frontend.js&py=3&rawInputLstJSON=%5B%5D&textReferences=false

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
            current_node = current_node.next
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
               exp: 0 <-> 2 <-> 1 <-> 3 <-> 4"""
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

my_dll = DoublyLinkedList(1)
my_dll.append(2)
my_dll.append(3)
my_dll.append(4)

print('my_dll before swap pairs: ')
my_dll.print_list()

my_dll.swap_pairs()

print('my_dll after swap pairs: ')

my_dll.print_list()
