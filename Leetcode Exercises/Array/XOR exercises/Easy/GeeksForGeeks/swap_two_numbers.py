"""
Given two variables, x, and y, swap two variables without using a third variable. 
"""

# #method1: using addition and subtraction

# x = 10
# y = 5

# # x becomes 15

# x = x + y

# # y becomes 10

# y = x - y

# # x becomes 5

# x = x - y

# print(x,y)

#method 2: using bitwise XOR

x = 10
y = 5

x = x ^ y #x becomes 15(1111)
y = x ^ y #y becomes 10(1010)
x = x ^ y #x becomes 5 (0101)

print(x, y)