"""
Given two numbers, the task is to check if two numbers are equal without using Arithmetic and Comparison Operators or String functions.
"""

def checkEqual(x, y):

    #we can use XOR, because XOR of 2 same numbers is Zero
    if ((x ^ y) ==0):
        print("Same")
    else:
        print("Not the same")


checkEqual(2, 2)