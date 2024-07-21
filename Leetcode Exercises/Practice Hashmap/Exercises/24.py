"""
Write a Python program to create a dictionary from a string.
Note: Track the count of the letters from the string.
Sample string : 'w3resource'
Expected output: {'w': 1, '3': 1, 'r': 2, 'e': 2, 's': 1, 'o': 1, 'u': 1, 'c': 1}
"""

string1 = 'w3resources'

my_dict = {}

for letter in string1:
    #we use the get method with a default value of 0 and then incrementing by 1
    my_dict[letter] = my_dict.get(letter, 0) + 1

print(my_dict)