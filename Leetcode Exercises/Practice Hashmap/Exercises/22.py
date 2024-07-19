"""
Write a Python program to find the highest 3 values of corresponding keys in a dictionary.
"""

my_dict = {'a': 500, 'b': 5874, 'c': 560, 'd': 400, 'e': 5874, 'f': 20}

my_keys = sorted(my_dict, key = my_dict.get, reverse=True)
print(my_keys[:3])