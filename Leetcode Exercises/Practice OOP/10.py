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
        return len(self.items) == 0
    

queue = Queue()

queue.enqueue(10)
queue.enqueue(20)
queue.enqueue(30)
queue.enqueue(40)
queue.enqueue(50)

print("Current queue:", queue.items)

dequeued_item = queue.dequeue()
print("Dequeued item:", dequeued_item)

dequeued_item = queue.dequeue()
print("Dequeued item:", dequeued_item)

print("Updated queue:", queue.items)