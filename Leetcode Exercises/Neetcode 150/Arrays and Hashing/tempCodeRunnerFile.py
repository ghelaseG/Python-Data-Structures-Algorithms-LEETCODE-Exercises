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