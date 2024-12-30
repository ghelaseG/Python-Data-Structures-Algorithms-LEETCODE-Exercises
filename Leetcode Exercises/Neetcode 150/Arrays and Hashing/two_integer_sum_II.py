"""
Given an array of integers numbers that is sorted in non-decreasing order.

Return the indices (1-indexed) of two numbers, [index1, index2], such that they add up to a given target number target and index1 < index2. Note that index1 and index2 cannot be equal, therefore you may not use the same element twice.

There will always be exactly one valid solution.

Your solution must use 
O
(
1
)
O(1) additional space.
"""
from typing import List

class Solution:
    def two_sum_II(self, numbers: List[int], target: int) -> List[int]:
        #part 1
        # for i in range(len(numbers)):
        #     for j in range(i + 1, len(numbers)):
        #         if numbers[i] + numbers[j] == target:
        #             return [i + 1, j + 1]
        # return []

        #part 2
        for i in range(len(numbers)):
            l, r = i + 1, len(numbers) - 1
            tempr = target - numbers[i]
            while l <= r:
                mid = l + (r - l) // 2
                if numbers[mid] == tempr:
                    return [i + 1, mid + 1]
                elif numbers[mid] < tempr:
                    l = mid + 1
                else:
                    r = mid - 1

        return []
     
numbers = [1,2,3,4]
target = 3

solution = Solution()
print(solution.two_sum_II(numbers, target))