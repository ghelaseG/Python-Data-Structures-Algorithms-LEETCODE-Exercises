"""
Write a Python program to create a dictionary from two lists without losing duplicate values.
Sample lists: ['Class-V', 'Class-VI', 'Class-VII', 'Class-VIII'], [1, 2, 2, 3]
Expected Output: defaultdict(<class 'set'>, {'Class-V': {1}, 'Class-VI': {2}, 'Class-VII': {2}, 'Class-VIII': {3}})
"""

from collections import defaultdict

class_list = ['Class-V', 'Class-VI', 'Class-VII', 'Class-VIII']
id_list = [1, 2, 2, 3]

#create a defaultdict with set as the default factory function

temp = defaultdict(set)

#iterate through pair elements using zip function
for key, value in zip(class_list, id_list):
    #add the value associated with the key in the temp dict
    temp[key].add(value)

print(temp)