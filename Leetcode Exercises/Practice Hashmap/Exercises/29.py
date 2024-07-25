"""
Write a Python program to remove spaces from dictionary keys.
"""

student_list = {'S  001': ['Math', 'Science'], 'S    002': ['Math', 'English']}


#we are going to use a dictionary comprehension to create a new dict
#we then iterate through the key value pairs
#we remove extra spaces using translate

new_dict = {x.translate({32: None}): y for x, y in student_list.items()}

print("New dictionary:", new_dict)