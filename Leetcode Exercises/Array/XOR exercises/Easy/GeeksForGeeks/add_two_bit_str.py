"""
Given two bit sequences as strings, write a function to return the addition of the two sequences. Bit strings can be of different lengths also. For example, if string 1 is “1100011” and second string 2 is “10”, then the function should return “1100101”. 
"""

def addBitStrings(str1, str2):
    ans = ''
    i = len(str1) - 1
    j = len(str2) - 1
    carry = 0
    while i >= 0 or j >= 0 or carry:
        if i >= 0:
            carry += ord(str1[i]) - ord('0')
            i = i - 1
        else:
            carry += 0

        if j >= 0:
            carry += ord(str2[j]) - ord('0')
            j = j - 1
        else:
            carry += 0

        ans = chr(ord('0')) + ans
        carry = carry // 2
    return ans