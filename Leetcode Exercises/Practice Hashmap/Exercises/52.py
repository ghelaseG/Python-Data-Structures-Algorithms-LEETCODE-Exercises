"""
Write a Python program to extract a list of values from a given list of dictionaries.
Original Dictionary:
[{'Math': 90, 'Science': 92}, {'Math': 89, 'Science': 94}, {'Math': 92, 'Science': 88}]
Extract a list of values from said list of dictionaries where subject = Science
[92, 94, 88]
Original Dictionary:
[{'Math': 90, 'Science': 92}, {'Math': 89, 'Science': 94}, {'Math': 92, 'Science': 88}]
Extract a list of values from said list of dictionaries where subject = Math
[90, 89, 92]
"""

marks = [{'Math': 90, 'Science': 92}, 
         {'Math': 89, 'Science': 94}, 
         {'Math': 92, 'Science': 88}]

def extract_value(lst, key):

    result = [dict[key] for dict in lst if key in dict]
    return result

subject = 'Science'

print(extract_value(marks, subject))

subject2 = 'Math'

print(extract_value(marks, subject2))

subject3 = 'Biology'

print(extract_value(marks, subject3))
