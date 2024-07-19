"""
Write a “C” function, int addOvf(int* result, int a, int b) If there is no overflow, the function places the resultant = sum a+b in “result” and returns 0. Otherwise, it returns -1. The solution of casting to long and adding to find detecting the overflow is not allowed.
Method 1 
There can be overflow only if signs of two numbers are same, and sign of sum is opposite to the signs of numbers. 
"""

def addOvf(result, a, b):
    result = a + b
    if a > 0 and b > 0 and result < 0:
        return -1
    elif a < 0 and b < 0 and result > 0:
        return -1
    else:
        return 0

res = -2147483646 
x = 2147483640
y = 11

print(addOvf(res, x, y))
