"""
Write a Python program to create a flat list of all the keys in a flat dictionary.
Sample Output:
Original dictionary elements:
{'Theodore': 19, 'Roxanne': 20, 'Mathew': 21, 'Betty': 20}
Create a flat list of all the keys of the said flat dictionary:
['Theodore', 'Roxanne', 'Mathew', 'Betty']
"""

def extract_keys(dictt):
    return list(dictt.keys())


students = {
    'Theodore': 19,
    'Roxanne': 20,
    'Mathew': 21,
    'Betty': 20
}

print(extract_keys(students))