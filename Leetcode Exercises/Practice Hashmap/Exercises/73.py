"""
Write a Python program to convert a list of dictionaries into a list of values corresponding to the specified key.
Sample Output:
Original list of dictionaries:
[{'name': 'Theodore', 'age': 18}, {'name': 'Mathew', 'age': 22}, {'name': 'Roxanne', 'age': 20}, {'name': 'David', 'age': 18}]
Convert a list of dictionaries into a list of values corresponding to the specified key:
[18, 22, 20, 18]
"""

def convert_to_list(dicts, key):
    return [value.get(key) for value in dicts]

#we create a list of dictionaries 
students = [
    {'name': 'Theodore', 'age': 18},
    {'name': 'Mathew', 'age': 22},
    {'name': 'Roxanne', 'age': 20},
    {'name': 'David', 'age': 18}
]

print(convert_to_list(students, 'age'))