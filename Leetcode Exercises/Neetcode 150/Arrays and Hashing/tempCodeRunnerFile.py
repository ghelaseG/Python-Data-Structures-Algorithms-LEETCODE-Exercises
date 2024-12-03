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