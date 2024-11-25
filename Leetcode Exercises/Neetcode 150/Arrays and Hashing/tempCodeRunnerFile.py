
from typing import List
from collections import defaultdict

class Solution:
    def group_anagrams(self, strs: List[str]) -> List[List[str]]: 
        result = defaultdict(list)

        for s in strs:
            #in the following we store counts of each character from a to z
            count = [0] * 26

            for char in s:
                #substract ASCII of c with "a" and store count of character in array
                count[ord(char) - ord("a")] += 1
                # Example ASCII(a) = 80, 80-80=0
                #         ASCII(b) = 81, 81-80=1
                #         ASCII(z) = 105, 105-80=25

            result[tuple(count)].append(s)

        return result.values()
    

strs = ["act","pots","tops","cat","stop","hat"]

solution = Solution()
print(solution.group_anagrams(strs))