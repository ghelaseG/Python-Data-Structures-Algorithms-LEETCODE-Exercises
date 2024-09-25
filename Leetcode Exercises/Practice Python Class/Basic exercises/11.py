"""
Write a Python class named Student with two attributes: student_id, student_name. Add a new attribute: student_class. Create a function to display all attributes and their values in the Student class.
"""

class Student:
    student_id = '2111'
    student_name = 'George Ghelase'

Student.student_class = '10D'


print(f"Student Attributes : {getattr(Student, 'student_id')}")    

for attr, items in Student.__dict__.items():
    if not attr.startswith('_'):
        print(f"{attr} -> {items}")