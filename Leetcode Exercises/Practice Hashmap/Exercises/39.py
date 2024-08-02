"""
Write a Python program to store dictionary data in a JSON file.
Original dictionary:
{'students': [{'firstName': 'Nikki', 'lastName': 'Roysden'}, {'firstName': 'Mervin', 'lastName': 'Friedland'}, {'firstName': 'Aron ', 'lastName': 'Wilkins'}], 'teachers': [{'firstName': 'Amberly', 'lastName': 'Calico'}, {'firstName': 'Regine', 'lastName': 'Agtarap'}]}
<class 'dict'>
Json file to dictionary:
{'students': [{'firstName': 'Nikki', 'lastName': 'Roysden'}, {'firstName': 'Mervin', 'lastName': 'Friedland'}, {'firstName': 'Aron ', 'lastName': 'Wilkins'}], 'teachers': [{'firstName': 'Amberly', 'lastName': 'Calico'}, {'firstName': 'Regine', 'lastName': 'Agtarap'}]}
"""

import json

d = {
    "students": [
        {"firstName": "Nikki", "lastName": "Roysden"},
        {"firstName": "Mervin", "lastName": "Friedland"},
        {"firstName": "Aron", "lastName": "Wilkins"}
    ],
    "teachers": [
        {"firstName": "Amberly", "lastName": "Calico"},
        {"firstName": "Regine", "lastName": "Agtarap"}
    ]
}

print(type(d))

with open('dictionay', 'w') as g:
    json.dump(d, g, indent = 4, sort_keys=True)

with open('dictionay') as f:
    data = json.load(f)

print(data)
