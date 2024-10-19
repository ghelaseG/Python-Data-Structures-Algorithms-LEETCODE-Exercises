"""
Write a Python program to create a class representing a queue data structure. Include methods for enqueueing and dequeueing elements.
"""


class Queue:

    def __init__(self):
        self.items = []

    def enqueue(self, item):
        return self.items.append(item)
    
    def dequeue(self):
        if not self.items.is_empty():
            return self.items.pop(0)
        else:
            raise IndexError("Cannot remove from an empty list")
        
    def is_empty(self):
        return len(self.items())