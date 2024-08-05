"""
Write a Python program to filter a dictionary based on values.
"""

marks = {'Cierra Vega': 175, 'Alden Cantrell': 180, 'Kierra Gentry': 165, 'Pierre Cox': 190}

#we're going to use a dictionary comprehension to create a new dict where values are greater than 170

new_dict = {key: value for (key, value) in marks.items() if value >= 170}

print(new_dict)