"""
Write a Python program to create a flat list of all the values in a flat dictionary.
Sample Output:
Original dictionary elements:
{'Theodore': 19, 'Roxanne': 20, 'Mathew': 21, 'Betty': 20}
Create a flat list of all the values of the said flat dictionary:
[19, 20, 21, 20]
"""

students = {
    'Theodore': 19,
    'Roxanne': 20,
    'Mathew': 21,
    'Betty': 20
}

def extract_values(dictt):
    return list(dictt.values())

print(extract_values(students))