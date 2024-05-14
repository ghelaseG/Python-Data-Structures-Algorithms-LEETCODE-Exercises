def __delete_node(self, current_node, value):
    if current_node == None:
        return None
    if value < current_node.value:
        current_node.left = self.__delete_node(current_node.left, value)
    elif value > current_node.value:
        current_node.right = self.__delete_node(current_node.right, value)
    else:
        if current_node.left == None and current_node.right == None:
            return None
        elif current_node.left == None:
            current_node = current_node.right
        elif current_node.right == None:
            current_node = current_node.left
        else:
    return current_node



def delete_node(self, value):
    self.root = self.__delete_node(self.root, value)