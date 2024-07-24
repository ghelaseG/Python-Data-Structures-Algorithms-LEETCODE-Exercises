"""
Given two numbers, the task is to check if two numbers are equal without using Arithmetic and Comparison Operators or String functions.
"""

# def checkEqual(x, y):

#     #we can use XOR, because XOR of 2 same numbers is Zero
#     if ((x ^ y) ==0):
#         print("Same")
#     else:
#         print("Not the same")


# checkEqual(2, 2)

def is_equal(num1, num2):
    mask = 1
    for i in range(32):
        if (num1 & mask) != (num2 & mask):
            return False
        mask <<= 1
    return True

print(is_equal(10, 10))
print(is_equal(20, 10))