"""
Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] where nums[i] + nums[j] + nums[k] == 0, and the indices i, j and k are all distinct.

The output should not contain any duplicate triplets. You may return the output and the triplets in any order.
"""
from typing import List
from collections import defaultdict

class Solution:
    def three_sum(self, nums: List[int]) -> List[List[int]]:
        #part 1
        # result = set()
        # nums.sort()
        # for i in range(len(nums)):
        #     for j in range(i + 1, len(nums)):
        #         for k in range( j + 1, len(nums)):
        #             if nums[i] + nums[j] + nums[k] == 0:
        #                 temps = [nums[i], nums[j], nums[k]]
        #                 result.add(tuple(temps))
        # return [list(i) for i in result]

        #part 2
        # nums.sort()
        # count = defaultdict(int)
        # for num in nums:
        #     count[num] += 1
        
        # result = []
        # for i in range(len(nums)):
        #     count[nums[i]] -= 1
        #     if i and nums[i] == nums[i - 1]:
        #         continue

        #     for j in range(i + 1, len(nums)):
        #         count[nums[j]] -= 1
        #         if j -1 > i and nums[j] == nums[j - 1]:
        #             continue
        #         target = -(nums[i] + nums[j])
        #         if count[target] > 0:
        #             result.append([nums[i], nums[j], target])
            
        #     for j in range(i + 1, len(nums)):
        #         count[nums[j]] += 1
        
        # return result

        #part 3
        result = []
        nums.sort()

        for i, a in enumerate(nums):
            if a > 0:
                break

            if i > 0 and a == nums[i - 1]:
                continue

            l, r = i + 1, len(nums) - 1
            while l < r:
                three_sum = a + nums[l] + nums[r]
                if three_sum > 0:
                    r -= 1
                elif three_sum < 0:
                    l += 1
                else:
                    result.append([a, nums[l], nums[r]])
                    l += 1
                    r -= 1
                    while nums[l] == nums[l - 1] and l < r:
                        l += 1
        return result

nums = [0,1,1]
solution = Solution()
print(solution.three_sum(nums))