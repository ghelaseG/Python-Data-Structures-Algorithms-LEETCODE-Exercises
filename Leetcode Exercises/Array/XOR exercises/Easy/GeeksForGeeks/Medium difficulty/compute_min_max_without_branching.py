"""
On some rare machines where branching is expensive, the below obvious approach to find minimum can be slow as it uses branching.
"""

# # Method 1: (use XOR and comparison operator)

# def min(x, y):
#     return y ^ ((x ^ y) & -(x < y))

# def max(x, y):
#     return x ^ ((x ^ y) & -(x < y))

# #this works because if x < y is True, then -(x < y) will be -1 which is all ones(111111111....)
# ##so y ^ ((x ^ y) & (1111111.....)) = y ^ x ^ y = x

# #otherwise, if x > y, then -(x < y) will be -(0) which is zero, so y ^ ((x ^ y) & 0) = y ^ 0 = y

# # Example:
# x = 15
# y = 6
# print('Min:')

# print(min(x, y))

# print('Max:')

# print(max(x, y))


# Method 2: Use subtraction and shift
import sys
"""
If we know that min <= (x - y) <= max , then we can use the following because is faster as it only runs one time

Min of x and y will be:
y + ((x - y) & ((x - y) >> (sizeof(int) * CHAR_BIT - 1))) :
This method shifts the subtraction of x and y by 31 (if size of int is 32). If (x - y) is smaller than 0,
then (x - y) >> 31 will be 1. But, if (x - y) is greater or equal to 0, then (x - y) >> 31 will be 0.
 - If (x >= y) we get minimum as y + (x - y) & 0 which is y.
 - If (x < y) we get minimum as y + (x - y) & 1 which is x.
"""

CHAR_BIT = 8
INT_BIT = sys.getsizeof(int())

def Min(x, y):
    return y + ((x - y) & ((x - y) >> (INT_BIT * CHAR_BIT - 1)))

def Max(x, y):
    return x - ((x - y) & ((x - y) >> (INT_BIT * CHAR_BIT - 1)))

x = 15
y = 10

print('Min: ')
print(Min(x, y))

print('Max: ')
print(Max(x, y))