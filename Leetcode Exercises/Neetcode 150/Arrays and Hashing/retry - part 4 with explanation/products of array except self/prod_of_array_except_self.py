"""
Given an integer array nums, return an array output where output[i] is the product of all the elements of nums except nums[i].

Each product is guaranteed to fit in a 32-bit integer.

Follow-up: Could you solve it in O(n) time without using the division operation?
"""

class Solution:
    def products_of_array_except_self(self, nums: list[int]) -> list[int]:

        # part 1 using brute force
        # n = len(nums)
        # result = [0] * n
        
        # for i in range(n):
        #     prod = 1
        #     for j in range(n):
        #         if i == j:
        #             continue
        #         prod *= nums[j]
            
        #     result[i] = prod
        
        # return result

        # part 2 using division
        product = 1
        zero_cnt = 0

        for num in nums:
            if num:
                product *= num
            else:
                zero_cnt += 1
        if zero_cnt > 1:
            return [0] * len(nums)
        
        result = [0] * len(nums)
        for i, c in enumerate(nums):
            if zero_cnt:
                result[i] = 0 if c else product
            else:
                result[i] = product // c
        return result

print(Solution().products_of_array_except_self(nums = [1,2,4,6]))


