"""
Write a Python script to sort (ascending and descending) a dictionary by value.
"""

def sort_dict_by_value(d, reverse=False):
    return dict(sorted(d.items(), key = lambda x: x[1], reverse=reverse))

print("Original dict:")

colors = {'Red': 1, 'Green': 3, 'Black': 5, 'White': 2, 'Pink': 4}

print(colors)

print('\nSort Ascending:')
print(sort_dict_by_value(colors))

print('\nSort Descending:')
print(sort_dict_by_value(colors, True))