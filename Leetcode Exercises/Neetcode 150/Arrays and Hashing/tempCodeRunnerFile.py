from typing import List

# class Solution:
#     def two_sum(self, nums: List[int], target: int) -> List[int]:
#         for i in range(len(nums)):
#             for j in range(i + 1, len(nums)):
#                 if nums[i] + nums[j] == target:
#                     return [i, j]
#         return []
    
# nums = [3,4,5,6] 
# target = 7

# solution =  Solution()
# print(solution.two_sum(nums, target))

class Solution:
    def two_sum(self, nums: List[int], target: int) -> List[int]:
        indices = {} #value is the index

        for i, j in enumerate(nums):
            indices[j] = i

        for i, j in enumerate(nums):
            difference = target - j
            if difference in indices and indices[difference] != i:
                return [i, indices[difference]]

nums = [3,4,5,6] 
target = 7
            
solution =  Solution()
print(solution.two_sum(nums, target))