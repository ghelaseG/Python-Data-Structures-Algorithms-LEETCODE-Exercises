from typing import List

class Solution:
    def has_duplicate(self, nums: List[int]) -> bool:
        #part 1 using brute force
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                if nums[i] == nums[j]:
                    return True
        
        return False
    
nums = [1, 2, 3, 3]
solution = Solution()
print(solution.has_duplicate(nums))