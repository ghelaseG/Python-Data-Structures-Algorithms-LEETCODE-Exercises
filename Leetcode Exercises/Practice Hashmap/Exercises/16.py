"""
Write a Python program to get a dictionary from an object's fields.
"""

# define a class with random name that inherits from the 'object' class

class my_dict_object(object):
    #define the constructor method '__init__' for initializing object attributes
    def __init__(self):
        self.x = 'Red'
        self.y = 'Green'
        self.z = 'Yellow'
    
    #define a method 'do_nothing' that doesn't perform any actions (placeholder)
    def do_nothing(self):
        pass

#create an instance test of the dictObj class
test = my_dict_object()

print(test.__hash__)

print(vars(test))

print(dir(test))