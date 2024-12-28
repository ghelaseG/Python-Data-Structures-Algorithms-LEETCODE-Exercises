from typing import List

class Solution:
    def two_sum_II(self, numbers: List[int], target: int) -> List[int]:
        for i in range(len(numbers)):
            for j in range(i + 1, len(numbers)):
                if numbers[i] + numbers[j] == target:
                    return [i + 1, j + 1]
        return []
    
numbers = [1,2,3,4]
target = 3

solution = Solution()
print(solution.two_sum_II(numbers, target))