"""
Write a Python program to sort a list alphabetically in a dictionary.
"""

num = {'n1': [2, 3, 1], 'n2': [5, 1, 2], 'n3': [3, 2, 4]}


#we are using a dictionary comprehension going through the key value pair

sorted_dict = {x: sorted(y) for x,y in num.items()}

print(sorted_dict)