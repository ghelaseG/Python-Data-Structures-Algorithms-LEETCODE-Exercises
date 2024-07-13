"""
Write a program that unsets the rightmost set bit of an integer. 
"""

def fun(n):

    return n & (n - 1)

n = 7

print("The number after unsetting the rightmost set bit", fun(n))