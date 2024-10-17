"""
Write a Python program to create a class representing a shopping cart. Include methods for adding and removing items, and calculating the total price.
"""

class ShoppingCart:

    #initialise the class with an empty list of items
    def __init__(self):
        self.items = []

    #add an item with a name and quantity to the shopping cart
    def add_item(self, item_name, qty):
        item = (item_name, qty)
        self.items.append(item)

    #remove an item with a specific name from the shopping cart
    def remove_item(self, item_name):
        for item in self.items:
            if item[0] == item_name:
                self.items.remove(item)
                break

    #calculate the total quantity of items
    def calculate_total(self):
        total = 0
        for item in self.items:
            total += item[1]
        return total
    
cart = ShoppingCart()

    