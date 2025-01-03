"""

Given two numbers x and y, and a range [l, r] where 1 <= l, r <= 32. The task is consider set bits of y in range [l, r] and set these bits in x also.

Input  : x = 10, y = 13, l = 2, r = 3
Output : x = 14
Binary representation of 10 is 1010 and 
that of y is 1101. There is one set bit
in y at 3'rd position (in given range). 
After we copy this bit to x, x becomes 1110
which is binary representation of 14.

Input  : x = 8, y = 7, l = 1, r = 2
Output : x = 11

"""

# #method 1

# #copy set bits in range [l, r] from y to x
# #note that x is passed by reference and modified by this function

# def copySetBits(x, y, l, r):
#     #l and r must be between 1 to 32
#     #(assuming ints are stored using 32 bits)
#     if (l < 1 or r > 32):
#         return x
    
#     #traverse in given range
#     for i in range(l, r + 1):

#         #find a mask(a number whose only set bit is at i'th position)
#         mask = 1 << (i - 1)

#         #if i'th bit is set in y, set i'th bit in x also
#         if ((y & mask) != 0):
#             x = x | mask
#     return x
    
# # example
# if __name__ == '__main__':
#     x = 10
#     y = 13
#     l = 1
#     r = 32
#     x = copySetBits(x, y, l, r)
#     print('Modified x is ', x)


# method 2

def copySetBits(x, y, l, r):

    # l and r must be between 1 and 32
    if (l < 1 or r > 32):
        return x
    
    # get the length of the mask
    maskLength = (int) ((1 << (r - l + 1)) - 1)

    # shift the mask to the required position '&' with y to get the set bits at between l and r in y
    mask = ((maskLength) << (l - 1)) & y
    x = x | mask
    return x

#Example
if __name__ == "__main__":
    
    x = 10
    y = 13
    l = 2
    r = 3
    x = copySetBits(x, y, l, r)
    print("Modified x is ", x)
