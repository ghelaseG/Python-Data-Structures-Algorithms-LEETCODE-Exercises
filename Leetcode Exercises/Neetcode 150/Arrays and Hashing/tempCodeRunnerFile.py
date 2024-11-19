from typing import List

class Solution:
    def hasDuplicates(self, nums: List[int]) ->bool:

        hashmap = {}

        for num in nums:
            if num in hashmap:
                return True
            else:
                hashmap[num] = 2
        
        return False
    
solution = Solution()
nums = [1,2,3,4,1,2]
print(solution.hasDuplicates(nums))