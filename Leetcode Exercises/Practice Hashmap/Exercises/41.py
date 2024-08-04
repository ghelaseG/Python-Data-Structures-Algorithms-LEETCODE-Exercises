"""
Write a Python program to drop empty items from a given dictionary.
Original Dictionary:
{'c1': 'Red', 'c2': 'Green', 'c3': None}
New Dictionary after dropping empty items:
{'c1': 'Red', 'c2': 'Green'}
"""

dict1 = {'c1': 'Red', 'c2': 'Green', 'c3': None}


my_dict = {key: value for (key,value) in dict1.items() if value is not None}

print(my_dict)