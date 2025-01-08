
from typing import List
class Solution:
    def trap(self, height: List[int]) -> int:

        # #part 1

        # if not height:
        #     return 0
        # n = len(height)
        # result = 0

        # for i in range(n):
        #     leftMax = rightMax = height[i]

        #     for j in range(i):
        #         leftMax = max(leftMax, height[j])
        #     for j in range(i + 1, n):
        #         rightMax = max(rightMax, height[j])

        #     result += min(leftMax, rightMax) - height[i]
        # return result

        #part 2
        # n = len(height)
        # if n == 0:
        #     return 0
        
        # leftMax = [0] * n
        # rightMax = [0] * n

        # leftMax[0] = height[0]
        # for i in range(1, n):
        #     leftMax[i] = max(leftMax[i - 1], height[i])
        
        # rightMax[n -  1] = height[n - 1]
        # for i in range(n - 2, -1, -1):
        #     rightMax[i] = max(rightMax[i + 1], height[i])
        
        # result = 0
        # for i in range(n):
        #     result += min(leftMax[i], rightMax[i])- height[i]
        
        # return result

        #part 3
        # if not height:
        #     return 0
        # stack = []
        # result = 0

        # for i in range(len(height)):
        #     while stack and height[i] >= height[stack[-1]]:
        #         mid = height[stack.pop()]
        #         if stack:
        #             right = height[i]
        #             left = height[stack[-1]]
        #             h = min(right, left) - mid
        #             w = i - stack[-1] - 1
        #             result += h * w
        #     stack.append(i)
        # return result

        #part 4
        if not height:
            return 0
        
        l, r = 0, len(height) - 1
        leftMax, rightMax = height[l], height[r]
        result = 0
        while l < r:
            if leftMax < rightMax:
                l += 1
                leftMax = max(leftMax, height[l])
                result += leftMax - height[l]
            else:
                r -= 1
                rightMax = max(rightMax, height[r])
                result += rightMax - height[r]
        return result

height = [0,2,0,3,1,0,1,3,2,1]    
solution = Solution()
print(solution.trap(height))