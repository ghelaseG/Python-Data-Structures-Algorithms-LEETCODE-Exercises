"""
Design an algorithm to encode a list of strings to a single string. The encoded string is then decoded back to the original list of strings.

Please implement encode and decode
"""
from typing import List

class Solution:
    def encode(self, strs: List[str]) -> str:
        ## part 1
        # if not strs:
        #     return ''
        # sizes = []
        # result = ''
        # for s in strs:
        #     sizes.append(len(s))
        # for sz in sizes:
        #     result += str(sz)
        #     result += ","
        # result += "#"
        # for s in strs:
        #     result += s
        # return result

        ## part 2
        result = ""
        for s in strs:
            result += str(len(s)) + "#" + s
        return result

    def decode(self, s: str) -> List[str]:
        ## part 1    
        # if not s:
        #     return []
        # sizes = []
        # result = []
        # i = 0
        # while s[i] != '#':
        #     curr = ''
        #     while s[i] != ",":
        #         curr += s[i]
        #         i += 1
        #     sizes.append(int(curr))
        #     i += 1
        # i += 1
        # for sz in sizes:
        #     result.append(s[i:i + sz])
        #     i += sz
        # return result
        
        ## part 2
        result = []
        i = 0

        while i < len(s):
            j = i
            while s[j] != '#':
                j += 1
            length = int(s[i:j])
            i = j + 1
            j = i + length
            result.append(s[i:j])
            i = j

        return result
    
strs = ["gg","love","you"]
gg = Solution().encode(strs)
print(gg)
gg2 = Solution().decode(gg)
print(gg2)    