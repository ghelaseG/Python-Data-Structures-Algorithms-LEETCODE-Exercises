"""
Write a Python program to get the maximum and minimum values of a dictionary.
"""

my_dict = {'x': 500, 'y': 5874, 'z': 560}


key_max = max(my_dict.keys(), key = (lambda k: my_dict[k]))

print(key_max)
print(my_dict[key_max])

key_min = min(my_dict.keys(), key = (lambda k: my_dict[k]))

print(key_min)
print(my_dict[key_min])