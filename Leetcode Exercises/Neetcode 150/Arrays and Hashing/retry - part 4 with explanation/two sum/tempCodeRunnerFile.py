"""
Given an array of integers nums and an integer target, return the indices i and j such that nums[i] + nums[j] == target and i != j.

You may assume that every input has exactly one pair of indices i and j that satisfy the condition.

Return the answer with the smaller index first.
"""
from typing import List

class Solution:
    def two_sum(self, nums: List[int], target: int) -> List[int]:
        # for i in range(len(nums)):
        #     for j in range(i+1, len(nums)):
        #         if nums[i] + nums[j] == target:
        #             return [i, j]
        # return []

        # # part 2 using sorting
        # A = []
        # for i, num in enumerate(nums):
        #     A.append([num, i])
        
        # A.sort()
        # i = 0
        # j = len(nums) - 1
        # while i < j:
        #     cur = A[i][0] + A[j][0]
        #     if cur == target:
        #         return [min(A[i][1], A[j][1]),
        #                 max(A[i][1], A[j][1])]
        #     elif cur < target:
        #         i += 1
        #     else:
        #         j -= 1
        # return []
        
        # # part 3 using hash map - two pass
        # indices = {}

        # for i, num in enumerate(nums):
        #     indices[num] = i
        
        # for i, num in enumerate(nums):
        #     diff = target - num
        #     if diff in indices and indices[diff] != i:
        #         return [i, indices[diff]]

        # part 4 using hash map - one pass
        indices = {}

        for i,num in enumerate(nums):
            diff = target - num
            if diff in indices:
                return [indices[diff], i]
            indices[num] = i

print(Solution().two_sum(nums=[3,4,5,6], target=7))
