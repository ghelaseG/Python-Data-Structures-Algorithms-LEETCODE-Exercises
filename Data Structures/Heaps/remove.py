def remove(self):
    if len(self.heap) == 0:
        return None
    
    if len(self.heap) == 1:
        return self.heap.pop()
    
    max_value = self.heap[0]
    self.heap[0] = self.heap.pop()
    self._sink_down(0)

    return max_value