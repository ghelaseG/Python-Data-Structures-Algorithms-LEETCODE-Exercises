"""
Write a Python program to create and display all combinations of letters, selecting each letter from a different key in a dictionary.
Sample data : {'1':['a','b'], '2':['c','d']}
Expected Output:
ac
ad
bc
bd
"""

d = {'1': ['a', 'b'], '2': ['c', 'd']}

result = [[]]

for key, value in d.items():
    result = [x + [y] for x in result for y in value]

print(result)