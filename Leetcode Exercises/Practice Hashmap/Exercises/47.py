"""
Write a Python program to split a given dictionary of lists into lists of dictionaries.
Original dictionary of lists:
{'Science': [88, 89, 62, 95], 'Language': [77, 78, 84, 80]}
Split said dictionary of lists into list of dictionaries:
[{'Science': 88, 'Language': 77}, {'Science': 89, 'Language': 78}, {'Science': 62, 'Language': 84}, {'Science': 95, 'Language': 80}]
"""


marks = {'Science': [88, 89, 62, 95], 'Language': [77, 78, 84, 80]}

def list_of_dicts(marks):
    keys = marks.keys()

    #next we use the zip function to transpose the lists of marks into tuples
    values = zip(*[marks[k] for k in keys])

    #we then create a list of dictionaries by zipping the keys and the transposed tuples
    result = [dict(zip(keys, v)) for v in values]
    return result

print(list_of_dicts(marks))