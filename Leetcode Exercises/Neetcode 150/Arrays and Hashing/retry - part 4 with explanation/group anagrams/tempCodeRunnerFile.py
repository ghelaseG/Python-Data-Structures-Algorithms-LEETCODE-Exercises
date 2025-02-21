"""
Given an array of strings strs, group all anagrams together into sublists. You may return the output in any order.

An anagram is a string that contains the exact same characters as another string, but the order of the characters can be different.
"""
from collections import defaultdict

class Solution():
    def group_anagrams(self, strs: list[str]) -> list[list[str]]:
        result = defaultdict(list)
        for s in strs:
            sorted_s = ''.join(sorted(s))
            result[sorted_s].append(s)
        return list(result.values())
    
print(Solution().group_anagrams(strs = ["act","pots","tops","cat","stop","hat"]))