"""
Given an integer array nums and an integer k, return the k most frequent elements within the array.

The test cases are generated such that the answer is always unique.

You may return the output in any order.
"""

class Solution:
    def top_k_element(self, nums: List[int], k: int) -> List[int]:
        count = {}
        for num in nums:
            count[num] = 1 + count.get(num, 0)
        
        arry = []
        for num, cnt in count.items():
            arry.append([cnt, num])
        arry.sort()

        result = []
        while len(result) < k:
            result.append(arry.pop()[1])
        return result