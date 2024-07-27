"""
Write a Python program to print a dictionary line by line.
"""

students = {'Aex': {'class': 'V', 'roll_id': 2}, 'Puja': {'class': 'V', 'roll_id': 3}}

#iterate through the dict 

for a in students:
    #print student name
    print(a)

    #iterate through the nested dict with the current student using a nested for loop
    for b in students[a]:
        #print the key and the corresponding value
        print(b, ':', students[a][b])