"""
Write a Python program to create a class representing a Circle. Include methods to calculate its area and perimeter.
"""

import math

class CircleRadius:
    #initialise the circle object with a given radius
    def __init__(self, radius):
        self.radius = radius
    
    #calculate and return the area of the circle: π * r^2
    def calculate_area(self):
        return math.pi * self.radius ** 2
    
    #calculate the perimeter(circumference) of the circle: 2π * r
    def calculate_circumference(self):
        return 2 * math.pi * self.radius
    
radius = float(input("Input the radius of the circle: "))
circle = CircleRadius(radius)

#calculate the area
area = circle.calculate_area()

#calculate the perimeter
perimeter = circle.calculate_circumference()

print("Area of the circle:", area)
print("Perimeter of the circle:", perimeter) 
