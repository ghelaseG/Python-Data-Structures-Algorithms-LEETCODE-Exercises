"""
Write a function to check if a given number is Sparse or not.

 - A number is said to be a sparse number if in the binary representation of the number no two or more consecutive bits are set.

 Example:
Input:  x  = 72
Output: true
Explanation:  Binary representation of 72 is 01001000. 
There are no two consecutive 1 in binary representation

Input:  x  = 12
Output: false
Explanation:  Binary representation of 12 is 1100. 
Third and fourth bits (from end) are set.
"""

def isSparse(n):
    if (n == 1):
        return True
    global prev
    while (n > 0):
        prev = n & 1
        n = n >> 1
        curr =  n & 1
        if (prev == curr and prev == 1):
            return False
        prev = curr
    
    return True

# Example
n = 72
if (isSparse(n)):
    print("Sparse")

else:
    print("Not Sparse")
