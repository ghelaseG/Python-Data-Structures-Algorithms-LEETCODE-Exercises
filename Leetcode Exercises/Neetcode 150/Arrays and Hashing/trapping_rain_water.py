"""
You are given an array non-negative integers height which represent an elevation map. Each value height[i] represents the height of a bar, which has a width of 1.

Return the maximum area of water that can be trapped between the bars.
"""

from typing import List
class Solution:
    def trap(self, height: List[int]) -> int:

        #part 1

        if not height:
            return 0
        n = len(height)
        result = 0

        for i in range(n):
            leftMax = rightMax = height[i]

            for j in range(i):
                leftMax = max(leftMax, height[j])
            for j in range(i + 1, n):
                rightMax = max(rightMax, height[j])

            result += min(leftMax, rightMax) - height[i]
        return result

height = [0,2,0,3,1,0,1,3,2,1]    
solution = Solution()
print(solution.trap(height))