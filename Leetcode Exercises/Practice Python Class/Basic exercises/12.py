"""
Write a Python class named Student with two instances student1, student2 and assign values to the instances' attributes. Print all the attributes of the student1, student2 instances with their values in the given format.
"""

class Student:
    school = 'Forward Thinking'
    address = '262 Park Lane, London'

student1 = Student()
student2 = Student()
student1.student_id = 'V12'
student1.student_name = 'Ernesto Mendez'
student2.student_id = 'V12'
student2.marks_language = 85
student2.marks_science = 93
student2.marks_math = 95
students = [student1, student2]

for student in students:
    print('\n')
    for attr in student.__dict__:
        print(f'{attr} -> {getattr(student, attr)}')
