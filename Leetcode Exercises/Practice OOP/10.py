"""
Write a Python program to create a class representing a queue data structure. Include methods for enqueueing and dequeueing elements.
"""


class Queue:

    def __init__(self):
        self.items = []

    def enqueue(self, item):
        return self.items.append(item)
    
    #we remove from the front of the queue
    def dequeue(self):
        if not self.is_empty():
            return self.items.pop(0)
        else:
            raise IndexError("Cannot remove from an empty queue")
        
    def is_empty(self):
        return len(self.items()) == 0