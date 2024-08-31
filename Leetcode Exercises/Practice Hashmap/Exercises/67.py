"""
Write a Python program to invert a given dictionary with non-unique hashable values.
Sample Output:
{8: ['Ora Mckinney', 'Mathew Gilbert'], 7: ['Theodore Hollandl', 'Mae Fleming', 'Ivan Little']}
"""
students = {
  'Ora Mckinney': 8,
  'Theodore Hollandl': 7,
  'Mae Fleming': 7,
  'Mathew Gilbert': 8,
  'Ivan Little': 7,
}

from collections import defaultdict

def transform(dicts):
    #create a dict with list as the default value for each key

    obj = defaultdict(list)

    #iterate through the key value pairs 
    for key, value in dicts.items():
        obj[value].append(key)
    
    #convert the defaultdict into a regular dictionary and return it
    return dict(obj)


print(transform(students))