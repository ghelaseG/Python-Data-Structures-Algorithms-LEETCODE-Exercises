"""
Given an array of strings strs, group all anagrams together into sublists. You may return the output in any order.

An anagram is a string that contains the exact same characters as another string, but the order of the characters can be different.
"""

from typing import List
from collections import defaultdict

class Solution:
    def group_anagrams(self, strs: List[str]) -> List[List[str]]:
        result = defaultdict(list)
        for i in strs:
            sorted_s = ''.join(sorted(i))
            result[sorted_s].append(i)
        return list(result.values())
    
strs = ["act","pots","tops","cat","stop","hat"]

solution = Solution()
print(solution.group_anagrams(strs))
