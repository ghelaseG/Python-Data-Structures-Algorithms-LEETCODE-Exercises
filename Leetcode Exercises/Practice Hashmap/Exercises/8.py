"""
Write a Python script to merge two Python dictionaries.
"""

#1st Solution

d1 = {'a': 100, 'b': 200}
d2 = {'x': 300, 'y': 100}

d = d1.copy()

d.update(d2)

print(d)

#2nd Solutin
print('\n2nd solution\n')

d3 = {'a': 100, 'b': 200}
d4 = {'x': 300, 'y': 100}

def merge_dictionaries(*dicts):
    
    result = dict()

    for d in dicts:
        result.update(d)
    
    return result

print(merge_dictionaries(d3, d4))

                       

