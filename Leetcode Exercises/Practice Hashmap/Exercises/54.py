"""
Write a Python program to get the depth of a dictionary.
"""

dic = {'a': 1, 'b': {'c': {'d': {}}}}

def dict_depth(d):
    # check if the input is a dictionary
    if isinstance(d, dict):
        # if d is a dictionary , return 1 plus the maximum depth of its values(recursively)
        return 1 + (max(map(dict_depth, d.values())) if d else 0)
    # if d is not a dictionary return 0 (indicating no nesting)
    return 0

print(dict_depth(dic))
