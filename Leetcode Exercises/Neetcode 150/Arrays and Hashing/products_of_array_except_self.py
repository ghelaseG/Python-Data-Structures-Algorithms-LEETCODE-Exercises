"""
Given an integer array nums, return an array output where output[i] is the product of all the elements of nums except nums[i].

Each product is guaranteed to fit in a 32-bit integer.

Follow-up: Could you solve it in 
O
(
n
)
O(n) time without using the division operation?
"""
# from typing import List

# class Solution:
#     def product_except_self(self, nums: List[int]) -> List[int]:
#         n = len(nums)
#         res = [0] * n

#         for i in range(n):
#             prod = 1
#             for j in range(n):
#                 if i == j:
#                     continue
#                 prod *= nums[j]
            
#             res[i] = prod
#         return res

# solution = Solution()

# nums = [1,2,4,6]

# print(solution.product_except_self(nums))

# part 2 using division

from typing import List

class Solution:
    def product_except_self(self, nums: List[int]) -> List[int]:
        prod, zero_cnt = 1, 0
        for num in nums:
            if num:
                prod *= num
            else:
                zero_cnt += 1
        if zero_cnt > 1: 
            return [0] * len(nums)
        
        res = [0] * len(nums)
        for i, c in enumerate(nums):
            if zero_cnt:
                res[i] = 0 if c else prod
            else:
                res[i] = prod // c
        return res
    
solution = Solution()

nums = [1,2,4,6]

print(solution.product_except_self(nums))