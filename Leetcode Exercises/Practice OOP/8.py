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

#example

cart.add_item("Papaya", 100)
cart.add_item("Guava", 200)
cart.add_item("Orange", 150)

#display the current item in the cart and calculate the total quantity
print("Current items in the cart:")
for item in cart.items:
    print(item[0], "-", item[1])

total_qty = cart.calculate_total()
print("Total Quantity:", total_qty)

#remove an item, display the new cart and calculate the total

cart.remove_item("Orange")
print("\nUpdated Items in the Cart after removing Orange:")
for item in cart.items:
    print(item[0], "-", item[1])

total_qty = cart.calculate_total()
print("Total Quantity:", total_qty)    