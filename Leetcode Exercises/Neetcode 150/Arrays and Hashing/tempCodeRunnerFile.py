from typing import List

class Solution:
    def product_except_self(self, nums: List[int]) -> List[int]:
        n = len(nums)
        res = [0] * n

        for i in range(n):
            prod = 1
            for j in range(n):
                if i == j:
                    continue
                prod *= nums[j]
            
            res[i] = prod
        return res

solution = Solution()

nums = [1,2,4,6]

print(solution.product_except_self(nums))

