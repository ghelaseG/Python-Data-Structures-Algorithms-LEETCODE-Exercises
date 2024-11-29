"""
Given an integer array nums and an integer k, return the k most frequent elements within the array.

The test cases are generated such that the answer is always unique.

You may return the output in any order.
"""
# from typing import List

# class Solution:
#     def topKFrequent(self, nums: List[int], k: int) -> List[int]:

#         count = {}
#         for num in nums:
#             count[num] = 1 + count.get(num, 0)

#         arr = []
#         for i, j in count.items():
#             arr.append([j, i])
#         arr.sort()

#         res = []
#         while len(res) < k:
#             res.append(arr.pop()[1])
#         return res
    
# nums = [1,2,2,3,3,3]
# k = 2

# solution = Solution()
# print(solution.topKFrequent(nums, k))

# #part 2 using heap

# import heapq
# from typing import List


# class Solution:
#     def top_k_frequent(self, nums: List[int], k: int) -> List[int]:

#         count = {}

#         for num in nums:
#             count[num] = 1 + count.get(num, 0)

#         heap = []
#         for num in count.keys():
#             heapq.heappush(heap, (count[num], num))
#             if len(heap) > k:
#                 heapq.heappop(heap)

#         res = []
#         for i in range(k):
#             res.append(heapq.heappop(heap)[i])
#         return res
    
# nums = [1,2,2,3,3,3]
# k = 2

# solution = Solution()
# print(solution.top_k_frequent(nums, k))



# part 3 using bucket sort

from typing import List

class Solution:
    def top_k_frequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        freq = [[] for i in range(len(nums) + 1)]

        for num in nums:
            count[num] = 1 + count.get(num, 0)
        for num, cnt in count.items():
            freq[cnt].append(num)

        res = []
        for i in range(len(freq) - 1, 0, -1):
            for num in freq[i]:
                res.append(num)
                if len(res) == k:
                    return res


nums = [1,2,2,3,3,3]
k = 2

solution = Solution()
print(solution.top_k_frequent(nums, k))
                
