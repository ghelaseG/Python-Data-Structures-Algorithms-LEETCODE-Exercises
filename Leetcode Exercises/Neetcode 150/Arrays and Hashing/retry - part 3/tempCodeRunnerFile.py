"""
Given an array of integers nums, return the length of the longest consecutive sequence of elements that can be formed.

A consecutive sequence is a sequence of elements in which each element is exactly 1 greater than the previous element. The elements do not have to be consecutive in the original array.

You must write an algorithm that runs in O(n) time.
"""
from typing import List
from collections import defaultdict

class Solution:
    def longest_consecutive_sequence(self, nums: List[int]) -> int:
        # part 1 using brute force
        # result = 0
        # store = set(nums)

        # for num in nums:
        #     streak = 0
        #     curr = num
        #     while curr in store:
        #         streak += 1
        #         curr += 1
        #     result = max(result, streak)
        # return result

        # part 2 using sorting
        # if not nums:
        #     return 0
        # result = 0
        # nums.sort()

        # curr = nums[0]
        # streak = 0
        # i = 0
        # while i < len(nums):
        #     if curr != nums[i]:
        #         curr = nums[i]
        #         streak = 0
        #     while i < len(nums) and nums[i] == curr:
        #         i += 1
        #     streak += 1
        #     curr += 1
        #     result = max(result, streak)
        # return result

        # part 3 using hash set
        # num_set =set(nums)
        # longest = 0

        # for num in num_set:
        #     if (num - 1) not in num_set:
        #         length = 1
        #         while (num + length) in num_set:
        #             length += 1
        #         longest = max(length, longest)
        # return longest

        # part 4 using hash map
        
        mp = defaultdict(int)
        result = 0

        for num in nums:
            if not mp[num]:
                mp[num] = mp[num - 1] + mp[num + 1]
                mp[num - mp[num - 1]] = mp[num]
                mp[num + mp[num + 1]] = mp[num]
                result = max(result, mp[num])
        return result
                                           

print(Solution().longest_consecutive_sequence(nums = [2,20,4,10,3,4,5]))
