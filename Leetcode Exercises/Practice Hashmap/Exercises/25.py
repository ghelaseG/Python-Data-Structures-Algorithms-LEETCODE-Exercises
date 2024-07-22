"""
Write a Python program to print a dictionary in table format.
"""

my_dict = {'C1': [1, 2, 3], 'C2': [5, 6, 7], 'C3': [9, 10, 11]}

#we can use a list comprehension to create a list of tuples 
#sort them by key value pairs 
#we use zip function to change the position of the rows and columns

for row in zip(*([key] + (value) for key, value in sorted(my_dict.items()))):
    # print each row of transposed data as spaced separated values
    print(*row)