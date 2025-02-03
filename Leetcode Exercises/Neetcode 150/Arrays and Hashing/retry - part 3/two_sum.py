"""
Given an array of integers nums and an integer target, return the indices i and j such that nums[i] + nums[j] == target and i != j.

You may assume that every input has exactly one pair of indices i and j that satisfy the condition.

Return the answer with the smaller index first.


"""
from typing import List

class Solution:
    def two_sum(self, nums: List[int], target: int) -> List[int]:
        # part 1 using brute force
        # for i in range(len(nums)):
        #     for j in range(i + 1, len(nums)):
        #         if nums[i] + nums[j] == target:
        #             return [i, j]
        
        # # part 2 using sorting
        # A = []
        # for i, num in enumerate(nums):
        #     A.append([num, i])
        
        # A.sort()
        # i, j = 0, len(nums) - 1
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

        # part 3 using hash map (two pass)
        # indices = {}

        # for i, n in enumerate(nums):
        #     indices[n] = i

        # for i, n in enumerate(nums):
        #     diff = target - n
        #     if diff in indices and indices[diff] != i:
        #         return [i, indices[diff]] 

        # part 4 using hash map - one pass
        prevMap = {}

        for i, n in enumerate(nums):
            diff = target - n
            if diff in prevMap:
                return [prevMap[diff], i]
            prevMap[n] = i
                           
nums = [4,5,6]
target = 10
print(Solution().two_sum(nums, target))

