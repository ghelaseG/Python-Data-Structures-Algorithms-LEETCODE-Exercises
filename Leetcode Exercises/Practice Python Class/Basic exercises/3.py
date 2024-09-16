"""
Write a Python program to create an instance of a specified class and display the namespace of the said instance.
"""

class Student:
    def __init__(self, student_id, student_name, class_name):
        self.student_id = student_id
        self.student_name = student_name
        self.class_name =  class_name

student = Student('D8', 'Georgian', 'D')
print(student.__dict__)