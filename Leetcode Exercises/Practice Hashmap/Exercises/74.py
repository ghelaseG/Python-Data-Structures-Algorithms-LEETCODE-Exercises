"""
Write a Python program to create a dictionary with the same keys as the given dictionary and values generated by running the given function for each value.
Sample Output:
Original dictionary elements:
{'Theodore': {'user': 'Theodore', 'age': 45}, 'Roxanne': {'user': 'Roxanne', 'age': 15}, 'Mathew': {'user': 'Mathew', 'age': 21}}
Dictionary with the same keys:
{'Theodore': 45, 'Roxanne': 15, 'Mathew': 21}
"""

#define a function that takes a dictionary 'obj' and a function 'fn'

def create_dict(obj, fn):
    #use a dictionary comprehension to apply the function 'fn' to each value in the 'obj' dict
    #the result is a new dictionary with the same keys, where each value is transformed by 'fn'
    return dict((k, fn(v)) for k, v in obj.items())

users = {
    'Theodore': {'user': 'Theodore', 'age': 45},
    'Roxanne': {'user': 'Roxanne', 'age': 15},
    'Mathew': {'user': 'Mathew', 'age': 21},
}

print(create_dict(users, lambda u: u['age']))