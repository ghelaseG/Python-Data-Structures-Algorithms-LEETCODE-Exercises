from typing import List

class Solution:
    def max_area(self, heights: List[int]) -> int:
        #part 1
        # result = 0
        # for i in range(len(heights)):
        #     for j in range(i + 1, len(heights)):
        #         result = max(result, min(heights[i], heights[j]) * (j - 1))
        # return result

        #part 2
        l, r = 0, len(heights) - 1
        result = 0

        while l < r:
            area = min(heights[l], heights[r]) * (r - l)
            result = max(result, area)
            if heights[l] <= heights[r]:
                l += 1
            else:
                r -= 1
        return result
    
height = [1,7,2,5,4,7,3,6]
solution = Solution()
print(solution.max_area(height))