"""
Given an integer array nums, return true if any value appears more than once in the array, otherwise return false.
"""

# class Solution:
#     def hasDuplicate(self, nums: list[int]) -> bool:
#         hashset = set()

#         for n in nums:
#             if n in hashset:
#                 return True
#             else:
#                 hashset.add(n)
#         return False

# solution = Solution()
# nums = [1,2,3,4,1,2]
# print(solution.hasDuplicate(nums))

#2nd try
from typing import List

class Solution:
    def hasDuplicates(self, nums: List[int]) ->bool:

        hashmap = {}

        for num in nums:
            if num in hashmap:
                return True
            else:
                hashmap[num] = 'again'
        
        return False
    
solution = Solution()
nums = [1,2,3,4,1,2]
print(solution.hasDuplicates(nums))