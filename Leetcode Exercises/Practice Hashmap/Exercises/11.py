"""
Write a Python program to multiply all the items in a dictionary.
"""

my_dict = {'data1': 100, 'data2': -54, 'data3': 247}

result = 1

for i in my_dict:
    result = result * my_dict[i]

print(result)