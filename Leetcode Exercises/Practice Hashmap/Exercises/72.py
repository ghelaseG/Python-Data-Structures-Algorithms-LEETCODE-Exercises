"""
Write a Python program to invert a dictionary with unique hashable values.
Sample Output:
{10: 'Theodore', 11: 'Mathew', 9: 'Roxanne'}
"""

def invert(dicts):
    return {value: key for key, value in dicts.items()}

students = {
    'Theodore': 10,
    'Mathew': 11,
    'Roxanne': 9,
}

print(invert(students))