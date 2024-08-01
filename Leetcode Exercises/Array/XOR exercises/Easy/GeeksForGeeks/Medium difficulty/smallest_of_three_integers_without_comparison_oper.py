"""
Write a program to find the smallest of three integers, without using any of the comparison operators. 
Let 3 input numbers be x, y and z.
Method 1 (Repeated Subtraction) 
Take a counter variable c and initialize it with 0. In a loop, repeatedly subtract x, y and z by 1 and increment c. The number which becomes 0 first is the smallest. After the loop terminates, c will hold the minimum of 3. 
"""

# # Method 1
# ## Take a counter variable c and initialize it with 0. In a loop, repeatedly subtract x, y and z by 1 and increment c. The number which becomes 0 first is the smallest. After the loop terminates, c will hold the minimum of 3. 

# def minimumInteger(x, y, z):
#     count = 0

#     while (x and y and z):
#         x = x - 1
#         y = y - 1
#         z = z - 1
#         count += 1

#     return count

# #Example
# x = 20
# y = 15
# z = 5
# print('Minimum of 3 numbers is: ', minimumInteger(x, y, z))

# Method 2 : using bit operations

CHAR_BIT = 8

#we create a function to find the minimum of x and y
def min(x, y):
    return y + ((x - y) & (x - y) >> (32 * CHAR_BIT - 1))

#function to find minimum of 3 numbers
def smallest(x, y, z):
    return min(x, min(y, z))


#Example:
x = 12
y = 15
z = 5
print(smallest(x, y, z))

