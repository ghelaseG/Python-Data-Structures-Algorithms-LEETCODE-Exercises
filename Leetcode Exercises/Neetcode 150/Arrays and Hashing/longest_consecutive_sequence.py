"""
Given an array of integers nums, return the length of the longest consecutive sequence of elements that can be formed.

A consecutive sequence is a sequence of elements in which each element is exactly 1 greater than the previous element. The elements do not have to be consecutive in the original array.

You must write an algorithm that runs in O(n) time.
"""
from typing import List

class Solution:
    def longest_consecutive(self, nums: List[int]) -> int:
        # #part 1
        # result = 0
        # store = set(nums)

        # for num in nums:
        #     streak, curr = 0, num
        #     while curr in store:
        #         streak += 1
        #         curr += 1
        #     result = max(result, streak)
        # return result


        # #part 2
        # if not nums:
        #     return 0
        # result = 0
        # nums.sort()

        # current, streak = nums[0], 0
        # i = 0
        # while i < len(nums):
        #     if current != nums[i]:
        #         current = nums[i]
        #         streak = 0
        #     while i < len(nums) and nums[i] == current:
        #         i += 1
        #     streak += 1
        #     current += 1
        #     result = max(result, streak)
        # return result


        #part 3

        # num_set = set(nums)
        # longest = 0

        # for num in num_set:
        #     if (num - 1) not in num_set:
        #         length = 1
        #         while (num + length) in num_set:
        #             length += 1
        #         longest = max(length, longest)
        # return longest


        #part 4
        from collections import defaultdict
        
        mp = defaultdict(int)
        result = 0

        for num in nums:
            if not mp[num]:
                mp[num] = mp[num - 1] + mp[num + 1] + 1
                mp[num - mp[num - 1]] = mp[num]
                mp[num + mp[num + 1]] = mp[num]
                result = max(result, mp[num])
        return result
    
solution = Solution()
nums = [2,20,4,10,3,4,5]
print(solution.longest_consecutive(nums))