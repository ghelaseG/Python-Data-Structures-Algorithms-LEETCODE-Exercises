"""
Write a Python function student_data () that will print the ID of a student (student_id). If the user passes an argument student_name or student_class the function will print the student name and class.
"""

def student_data(student_id, **kwargs):
    print(f'\nStudent ID: {student_id}')
    if 'student_name' in kwargs:
        print(f"Student Name: $ {kwargs['student_name']}")

    if 'student_name' and 'student_class' in kwargs:
        print(f"\nStudent Name: $ {kwargs['student_name']}")
        print(f"Student Class: $ {kwargs['student_class']}")

student_data(student_id='SV1111', student_name = 'George George')

student_data(student_id='GG123', student_name = 'Geo Ghelase', student_class ='10D')