"""
Given an array of strings strs, group all anagrams together into sublists. You may return the output in any order.

An anagram is a string that contains the exact same characters as another string, but the order of the characters can be different.
"""
from collections import defaultdict
from typing import List

class Solution:

    def group_anagram(self, strs: List[str]) -> List[List[str]]:
        result = defaultdict(list)
        for s in strs:
            sorted_str = ' '.join(sorted(s))
            result[sorted_str].append(s)
        return list(result.values())
    
strs = ["act","pots","tops","cat","stop","hat"]
solution = Solution()
print(solution.group_anagram(strs))
