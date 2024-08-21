"""
Write a Python program to get all combinations of key-value pairs in a given dictionary.
Original Dictionary:
{'V': [1, 4, 6, 10], 'VI': [1, 4, 12], 'VII': [1, 3, 8]}
Combinations of key-value pairs of the said dictionary:
[{'V': [1, 4, 6, 10], 'VI': [1, 4, 12]}, {'V': [1, 4, 6, 10], 'VII': [1, 3, 8]}, {'VI': [1, 4, 12], 'VII': [1, 3, 8]}]
Original Dictionary:
{'V': [1, 3, 5], 'VI': [1, 5]}
Combinations of key-value pairs of the said dictionary:
[{'V': [1, 3, 5], 'VI': [1, 5]}]
"""

# use itertools module for his combination function
import itertools

def test(dict):
    #generate all combination of key value pairs in the dictionary
    #convert each combination into a dictionary and return a list of dictionaries
    result = list(map(dict, itertools.combinations(dict.items(), 2)))
    return result

students = {'V': [1, 4, 6, 10], 'VI': [1, 4, 12], 'VII': [1, 3, 8]}

print("Original dict:")
print(students)

print("Combinations of key value pairs:")
print(test(students))