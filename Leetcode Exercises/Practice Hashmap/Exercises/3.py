"""
Write a Python script to concatenate the following dictionaries to create a new one.

Sample Dictionary :
dic1={1:10, 2:20}
dic2={3:30, 4:40}
dic3={5:50,6:60}
Expected Result : {1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60}
"""

dic1 = {1:10, 2:20}
dic2 = {3:30, 4:40}
dic3 = {5:50, 6:60}

# dic4 = {}

# for i in (dic1, dic2, dic3):
#     dic4.update(i)

# print(dic4)

# or

merged = {**dic1, **dic2, **dic3}
print(merged)