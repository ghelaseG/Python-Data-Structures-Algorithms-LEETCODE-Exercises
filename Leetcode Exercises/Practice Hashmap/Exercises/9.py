"""
Write a Python program to iterate over dictionaries using for loops.
"""

d = {'Red': 1, 'Green': 2, 'Blue': 3}

for key, value in d.items():
    print(key, 'corresponds to: ', d[key])
    print(key,":", value)
