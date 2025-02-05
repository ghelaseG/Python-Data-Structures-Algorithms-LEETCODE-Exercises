"""
Given an integer array nums and an integer k, return the k most frequent elements within the array.

The test cases are generated such that the answer is always unique.

You may return the output in any order.
"""

from typing import List
import heapq

class Solution:
    def top_k_frequent_element(self, nums: List[int], k: int) -> List[int]:
        #part 1 using sorting

        # count = {}
        # for num in nums:
        #     count[num] = 1 + count.get(num, 0)
        
        # arr = []
        # for num, cnt in count.items():
        #     arr.append([cnt, num])
        # arr.sort()

        # result = []
        # while len(result) < k:
        #     result.append(arr.pop()[1])
        # return result

        # part 2 using heap
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

print(Solution().top_k_frequent_element(nums = [1,2,2,3,3,3], k = 2))