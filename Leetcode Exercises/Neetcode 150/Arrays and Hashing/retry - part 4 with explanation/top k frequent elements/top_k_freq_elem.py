"""
Given an integer array nums and an integer k, return the k most frequent elements within the array.

The test cases are generated such that the answer is always unique.

You may return the output in any order.
"""
import heapq

class Solution:
    def top_k_frequent_element(self, nums: list[int], k: int) -> list[int]:

        # part 1 using sorting
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

        # count = {}
        # for num in nums:
        #     count[num] = 1 + count.get(num, 0)

        # heap = []
        # for num in count.keys():
        #     heapq.heappush(heap, (count[num], num))
        #     if len(heap) > k:
        #         heapq.heappop(heap)
        
        # result = []
        # for i in range(k):
        #     result.append(heapq.heappop(heap)[1])
        # return result

        # part 3 using bucket sort

        count = {}
        freq = [[] for i in range(len(nums) + 1)]

        for num in nums:
            count[num] = 1 + count.get(num, 0)
        for num, cnt in count.items():
            freq[cnt].append(num)
        
        result = []
        for i in range(len(freq) - 1, 0, -1):
            for num in freq[i]:
                result.append(num)
                if len(result) == k:
                    return result

print(Solution().top_k_frequent_element(nums = [1,1,1,2,3,3], k = 2))