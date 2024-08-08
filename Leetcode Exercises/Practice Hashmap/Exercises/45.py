"""
Write a Python program to verify that all values in a dictionary are the same.
Original Dictionary:
{'Cierra Vega': 12, 'Alden Cantrell': 12, 'Kierra Gentry': 12, 'Pierre Cox': 12}
Check all are 12 in the dictionary.
True
Check all are 10 in the dictionary.
False
"""

students = {'Cierra Vega': 12, 'Alden Cantrell': 12, 'Kierra Gentry': 12, 'Pierre Cox': 12}

def value_check(students, n):
    result = all(x == n for x in students.values())
    return result

n = 12

print("\nCheck all are", n,"in the dictionary")
print(value_check(students, n))

n = 10

print("\nCheck all are", n,"in the dictionary")
print(value_check(students, n))

