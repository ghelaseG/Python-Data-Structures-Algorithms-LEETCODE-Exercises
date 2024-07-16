"""
Write a Python program to remove duplicates from the dictionary.
"""

# let's create a nested dictionary

student_data = {
    'id1': {
        'name': ['Sara'],
        'class': ['V'],
        'subject_integration': ['english, math, science']
    },
    'id2': {
        'name': ['David'],
        'class': ['V'],
        'subject_integration': ['english, math, science']
    },
    'id3': {
        'name': ['Sara'],
        'class': ['V'],
        'subject_integration': ['english, math, science']
    },
    'id4': {
        'name': ['Surya'],
        'class': ['V'],
        'subject_integration': ['english, math, science']
    }
}

print(student_data['id1'])

#create empty dict
result = {}

#iterate through the key-value pairs
for key, value in student_data.items():
    #check if the current value is not in the result dict
    if value not in result.values():
        #if not, add it to result with the corresponding key
        result[key] = value

print(result)