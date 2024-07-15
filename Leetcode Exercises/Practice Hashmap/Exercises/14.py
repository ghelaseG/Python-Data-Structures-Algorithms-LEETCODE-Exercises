"""
Write a Python program to sort a given dictionary by key.
"""

def sort_dict_by_keys(my_dict):
    
    return dict(sorted(my_dict.items()))

students = { 'name1': 'Theodore', 'name2': 'Mathew', 'name4': 'Roxanne', 'name3': 'David' }

print(sort_dict_by_keys(students))