"""
Given an integer x, write a C function that returns true if binary representation of x is palindrome else return false.
For example a numbers with binary representation as 10..01 is palindrome and number with binary representation as 10..00 is not palindrome.
The idea is similar to checking a string is palindrome or not. We start from leftmost and rightmost bits and compare bits one by one. If we find a mismatch, then return false. 
"""

# method 1

import sys

# the next function returns true if the k'th bit in x is set (or 1)
## for example, if x (0010) is 2 and k is 2, then it returns true

def isKthBitSet(x, k):
    if ((x & (1 << (k - 1))) != 0):
        return True
    else:
        return False
    
# the next function returns true if binary representation of x is palindrome
## for example: 10000...001 is a palindrome
    
def isPalindrome(x):
    l = 1 #initialize left position
    r = 2 * 8 #initialize right position

    # one by one compare the bits
    while (l < r):
        if (isKthBitSet(x, l) != isKthBitSet(x, r)):
            return False
        l += 1
        r -= 1

    return True

# example
if __name__ == '__main__':
    x = 1 << 15 + 1 << 16
    print(int(isPalindrome(x)))
    x = 1 << 31 + 1
    print(int(isPalindrome(x)))
