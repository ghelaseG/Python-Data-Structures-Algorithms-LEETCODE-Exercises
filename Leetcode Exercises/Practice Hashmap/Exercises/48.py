"""
Write a Python program to remove a specified dictionary from a given list.
Original list of dictionary:
[{'id': '#FF0000', 'color': 'Red'}, {'id': '#800000', 'color': 'Maroon'}, {'id': '#FFFF00', 'color': 'Yellow'}, {'id': '#808000', 'color': 'Olive'}]
Remove id #FF0000 from the said list of dictionary:
[{'id': '#800000', 'color': 'Maroon'}, {'id': '#FFFF00', 'color': 'Yellow'}, {'id': '#808000', 'color': 'Olive'}]
"""

colors = [
    {"id": "#FF0000", "color": "Red"},
    {"id": "#800000", "color": "Maroon"},
    {"id": "#FFFF00", "color": "Yellow"},
    {"id": "#808000", "color": "Olive"}
]

def remove_dictionary(colors, r_id):
    #use a list comprehension to filter out dictionaries with an 'id' not equal to r_id
    ## the filtered result is assigned back to the colors list, effectively removing the dictionary with the speciefied 'id'
    colors[:] = [d for d in colors if d.get('id') != r_id]
    return colors

r_id = "#FF0000"

print(remove_dictionary(colors, r_id))