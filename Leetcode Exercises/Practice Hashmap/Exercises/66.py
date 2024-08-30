"""
Write a Python program to check if a specific key and a value exist in a dictionary.
Original dictionary:
[{'student_id': 1, 'name': 'Jean Castro', 'class': 'V'}, {'student_id': 2, 'name': 'Lula Powell', 'class': 'V'}, {'student_id': 3, 'name': 'Brian Howell', 'class': 'VI'}, {'student_id': 4, 'name': 'Lynne Foster', 'class': 'VI'}, {'student_id': 5, 'name': 'Zachary Simon', 'class': 'VII'}]
Check if a specific Key and a value exist in the said dictionary:
True
True
True
False
False
False
"""

students = [
    {'student_id': 1, 'name': 'Jean Castro', 'class': 'V'},
    {'student_id': 2, 'name': 'Lula Powell', 'class': 'V'},
    {'student_id': 3, 'name': 'Brian Howell', 'class': 'VI'},
    {'student_id': 4, 'name': 'Lynne Foster', 'class': 'VI'},
    {'student_id': 5, 'name': 'Zachary Simon', 'class': 'VII'}
]

def check(dicts, key, value):
    #check if any sub dictionary in the list dicts has the given key with the specified value
    if any(dictt[key] == value for dictt in dicts):
        return True
    return False

print(check(students, 'student_id', 1))
print(check(students, 'name', 'Brian Howell'))
print(check(students, 'class', 'VII'))
print(check(students, 'class', 'I'))
print(check(students, 'name', 'Brian Howelll'))
print(check(students, 'student_id', 11)) 