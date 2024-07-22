"""
Given two integers, find XOR of them without using the XOR operator, i.e., without using ‘^‘ in C/C++.
"""

# def XorResult(x, y):
#     result = 0 #initialise result 

#     #we assume a 32 bit integer
#     for i in range(31, -1, -1):

#         #find current bits in x and y
#         b1 = x & (1 << i)
#         b2 = y & (1 << i)
#         b1 = min(b1, 1)
#         b2 = min(b2, 1)

#         #if both are 1 then is equal to 0,
#         #otherwise xor is same as or

#         xoredBit = 0
#         if (b1 & b2):
#             xoredBit = 0
#         else:
#             xoredBit = (b1 | b2)

#         #update result
#         result <<= 1
#         result |= xoredBit
    
#     return result

# #example

# x = 3
# y = 5
# print("XOR is:", XorResult(x, y))

#2nd Approach

# def myXOR(x, y):
#     return ((x | y) & ( ~x | ~y ))

# #Example:
# x = 3
# y = 5
# print('XOR is:', myXOR(x, y))

#3rd Approach

# def myXOR(x, y):
#     return (x & (~y)) | ((~x) & y)

# x = 3
# y = 5
# print('XOR is:', myXOR(x, y))

#4th Approach

def myXOR(x, y):
    return (x + y - (2 * (x & y)))

x = 3
y = 5
print('XOR is:', myXOR(x, y))