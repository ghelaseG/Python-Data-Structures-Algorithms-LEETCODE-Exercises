"""
On some rare machines where branching is expensive, the below obvious approach to find minimum can be slow as it uses branching.
"""

# Method 1: (use XOR and comparison operator)

def min(x, y):
    return y ^ ((x ^ y) & -(x < y))

def max(x, y):
    return x ^ ((x ^ y) & -(x < y))

#this works because if x < y is True, then -(x < y) will be -1 which is all ones(111111111....)
##so y ^ ((x ^ y) & (1111111.....)) = y ^ x ^ y = x

#otherwise, if x > y, then -(x < y) will be -(0) which is zero, so y ^ ((x ^ y) & 0) = y ^ 0 = y

# Example:
x = 15
y = 6
print('Min:')

print(min(x, y))

print('Max:')

print(max(x, y))