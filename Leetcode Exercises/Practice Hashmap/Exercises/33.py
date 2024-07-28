"""
Write a Python program to check if multiple keys exist in a dictionary.
"""

student = {
  'name': 'Alex',
  'class': 'V',
  'roll_id': '2',
  'name': 'George'
}

print(student.keys() >= {'class', 'name'})

# or

if all (k in student for k in ('class', 'roll_id')):
    print("They're there!")