"""
Given an integer array nums and an integer k, return the k most frequent elements within the array.

The test cases are generated such that the answer is always unique.

You may return the output in any order.
"""
import heapq
from typing import List

class Solution:
    def top_k_element(self, nums: List[int], k: int) -> List[int]:
        # count = {}
        # for num in nums:
        #     count[num] = 1 + count.get(num, 0)
        
        # arry = []
        # for num, cnt in count.items():
        #     arry.append([cnt, num])
        # arry.sort()

        # result = []
        # while len(result) < k:
        #     result.append(arry.pop()[1])
        # return result

        #Part 2
        count = {}
        for num in nums:
            count[num] = 1 + count.get(num, 0)
        
        heap = []
        for num in count.keys():
            heapq.heappush(heap, (count[num], num))
            if len(heap) > k:
                heapq.heappop(heap)
        
        result = []
        for i in range(k):
            result.append(heapq.heappop(heap)[1])
        return result

nums = [1,2,2,3,3,3]
k = 2
print(Solution().top_k_element(nums, k))    
