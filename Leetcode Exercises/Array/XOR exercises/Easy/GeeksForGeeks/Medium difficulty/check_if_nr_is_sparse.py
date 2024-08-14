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
# method 1

# def isSparse(n):
#     if (n == 1):
#         return True
#     global prev
#     while (n > 0):
#         prev = n & 1
#         n = n >> 1
#         curr =  n & 1
#         if (prev == curr and prev == 1):
#             return False
#         prev = curr
    
#     return True

# # Example
# n = 72
# if (isSparse(n)):
#     print("Sparse")

# else:
#     print("Not Sparse")


# method 2

"""
If we observe carefully, then we can notice that if we can use bitwise AND of the binary representation of the “given number, then it’s “right-shifted number”(i.e., half the given number) to figure out whether the number is sparse or not. The result of AND operator would be 0 if the number is sparse and non-zero if not sparse.
"""

def checkSparse(n):

    # n is not sparse if there is set in AND of n and n/2 (n >> 1)

    if (n & (n >> 1)):
        return 0
    
    return 1

if __name__ == "__main__":

    print(checkSparse(72))
    print(checkSparse(12))
    print(checkSparse(2))
    print(checkSparse(30))