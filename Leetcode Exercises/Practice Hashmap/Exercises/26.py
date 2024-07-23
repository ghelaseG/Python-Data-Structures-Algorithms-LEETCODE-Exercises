"""
Write a Python program to count the values associated with a key in a dictionary.
Expected Output:
6
2
"""

student = [{'id': 1, 'success': True, 'name': 'Lary'},
 {'id': 2, 'success': False, 'name': 'Rabi'},
 {'id': 3, 'success': True, 'name': 'Alex'}]

#print the total of id's
print(sum(d['id'] for d in student))

#print the total of success
print(sum(d['success'] for d in student))