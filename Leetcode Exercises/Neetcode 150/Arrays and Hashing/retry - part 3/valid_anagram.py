"""
Given two strings s and t, return true if the two strings are anagrams of each other, otherwise return false.

An anagram is a string that contains the exact same characters as another string, but the order of the characters can be different.
"""

class Solution:
    def chech_is_anagram(self, s: str, t: str) -> bool:
        # # part 1
        # if len(s) != len(t):
        #     return False
        
        # return sorted(s) == sorted(t)
        
        # part 2
        if len(s) != len(t):
            return False
        
        countS = {}
        countT = {}

        for i in range(len(s)):
            countS[s[i]] = 1 + countS.get(s[i], 0)
            countT[t[i]] = 1 + countT.get(t[i], 0)
        return countS == countT
    
s = "racecar"
t = "carrace"
print(Solution().chech_is_anagram(s, t))