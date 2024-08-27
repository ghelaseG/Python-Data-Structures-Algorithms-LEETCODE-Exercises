"""
Write a Python program to convert a given list of lists to a dictionary.
Original list of lists:
[[1, 'Jean Castro', 'V'], [2, 'Lula Powell', 'V'], [3, 'Brian Howell', 'VI'], [4, 'Lynne Foster', 'VI'], [5, 'Zachary Simon', 'VII']]
Convert the said list of lists to a dictionary:
{1: ['Jean Castro', 'V'], 2: ['Lula Powell', 'V'], 3: ['Brian Howell', 'VI'], 4: ['Lynne Foster', 'VI'], 5: ['Zachary Simon', 'VII']}
"""

def convert_list_to_dict(items):

    #use a dictionary comprehension to transform the list into a dictionary,
    #where the first element is a key, and the rest are values

    result = {item[0] : item[1:] for item in items}
    return result


students = [
    [1, 'Jean Castro', 'V'],
    [2, 'Lula Powell', 'V'],
    [3, 'Brian Howell', 'VI'],
    [4, 'Lynne Foster', 'VI'],
    [5, 'Zachary Simon', 'VII']
]

print("New Conversion:")
print(convert_list_to_dict(students))