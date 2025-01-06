"""
You are given an integer array heights where heights[i] represents the height of the i th bar.

You may choose any two bars to form a container. Return the maximum amount of water a container can store.
"""
from typing import List

class Solution:
    def max_area(self, heights: List[int]) -> int:
        result = 0
        for i in range(len(heights)):
            for j in range(i + 1, len(heights)):
                result = max(result, min(heights[i], heights[j]) * (j - 1))
        return result

height = [1,7,2,5,4,7,3,6]
solution = Solution()
print(solution.max_area(height))