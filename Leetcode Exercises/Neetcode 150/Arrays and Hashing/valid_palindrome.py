"""
Given a string s, return true if it is a palindrome, otherwise return false.

A palindrome is a string that reads the same forward and backward. It is also case-insensitive and ignores all non-alphanumeric characters.
"""

class Solution:
    def isPlalindrome(self, s: str) -> bool:

        new_string = ''
        for c in s:
            if c.isalnum():
                new_string += c.lower()
        return new_string == new_string[::-1]
    
s = "Was it a car or a cat I saw?"
solution = Solution()
print(solution.isPlalindrome(s))