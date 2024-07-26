"""
Write a Python program to get the top three items in a shop.
Sample data: {'item1': 45.50, 'item2':35, 'item3': 41.30, 'item4':55, 'item5': 24}
Expected Output:
item4 55
item1 45.5
item3 41.3
"""

my_dict = {'item1': 45.50, 'item2': 35, 'item3': 41.30, 'item4': 55, 'item5': 24}

dict_view = [ (value, key) for key, value in my_dict.items() ]
#print(dict_view)
dict_view.sort(reverse=True)
#print(dict_view)
for value, key in dict_view[:3]:
    print(f"{key} {value}")