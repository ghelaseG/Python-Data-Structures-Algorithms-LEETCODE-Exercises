"""
Given two strings s and t, return true if the two strings are anagrams of each other, otherwise return false.

An anagram is a string that contains the exact same characters as another string, but the order of the characters can be different.
"""

class Solution:
    def chech_is_anagram(self, s: str, t: str) -> bool:
        # part 1
        if len(s) != len(t):
            return False
        
        return sorted(s) == sorted(t)

s = "racecar"
t = "carrace"
print(Solution().chech_is_anagram(s, t))