"""
Write a Python program to create a class that represents a shape. Include methods to calculate its area and perimeter. Implement subclasses for different shapes like circle, triangle, and square.
"""

import math

#define a base class

class Shape:
    #placeholder method for calculating area
    def calculate_area(self):
        pass

    #placeholder method for calculating perimeter
    def calculate_perimeter(self):
        pass

#define a derived class called Circle, which inherits from the Shape class
class Circle(Shape):

    def __init__(self, radius):
        self.radius = radius

    #calculate and return the area of the circle using the formula: π * r^2
    def calculate_area(self):
        return math.pi * self.radius ** 2
    
    #calculate the perimeter using: 2π * r
    def calculate_perimeter(self):
        return 2 * math.pi * self.radius
    
class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width
    
    #calculate the area of the rectangle using: length * width
    def calculate_area(self):
        return self.length * self.width
    
    #use this formula to calculate the perimeter: 2 * (length + width)
    def calculate_perimeter(self):
        return 2 * (self.length + self.width)
    

class Triangle(Shape):
    def __init__(self, base, height, side1, side2, side3):
        self.base = base
        self.height = height
        self.side1 = side1
        self.side2 = side2
        self.side3 = side3
    
    #formula for area: 0.5 * base * height
    def calculate_area(self):
        return 0.5 * self.base * self.height
    
    #formula for perimeter: add the length of its three sides
    def calculate_perimeter(self):
        return self.side1 + self.side2 + self.side3
    
# Examples:
    
## Create a Circle object with a given radius and calculate its area and perimeter

r = 7
circle = Circle(r)
circle_area = circle.calculate_area()
circle_perimeter = circle.calculate_perimeter()

print("Radius of the circle:", r)
print("Circle Area:", circle_area)
print("Circle Perimeter:", circle_perimeter)