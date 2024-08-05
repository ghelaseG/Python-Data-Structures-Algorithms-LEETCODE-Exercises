"""
Write a function that, for a given no n, finds a number p which is greater than or equal to n and is the smallest power of 2. 
"""

# method 1: using log2(number) 

## calculate the log2N and store it into a variable 
## check if pow(2, a) is equal to N
        # return N
## otherwise return pow(2, a + 1)

import math

# def nearestPowerOf2(N):
#     # calculate log 2 of N
#     a = int(math.log2(N))

#     # if 2 pow a is equal to N, return N
#     if 2**a == N:
#         return N
    
#     # else, return 2 pow (a + 1)
#     return 2**(a + 1)

# # main function
# if __name__ == "__main__":
#     # input number
#     n = 10
#     print(nearestPowerOf2(n))

def nearestPowerOf2(n):
    count = 0

    #if n is zero then:
    if (n and not(n & (n - 1))):
        return n
    
    #else keep shifting n until it becomes zero and count no of shifts
    while (n != 0):
        n >>= 1
        count += 1

    return 1 << count

n = 4

print(nearestPowerOf2(n))