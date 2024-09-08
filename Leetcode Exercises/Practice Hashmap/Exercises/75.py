"""
Write a Python program to find all keys in a dictionary that have the given value.
Sample Output:
Original dictionary elements:
{'Theodore': 19, 'Roxanne': 20, 'Mathew': 21, 'Betty': 20}
Find all keys in the said dictionary that have the specified value:
['Roxanne', 'Betty']
"""

def test(dict, val):
    #use a list comprehension to find all the keys in the dictionary where the corresponding value is equal to 'val'
    return list(key for key, value in dict.items() if value == val)

students = {
    'Theodore': 19,
    'Roxanne': 20,
    'Mathew': 21,
    'Betty': 20
}

print(test(students, 20))