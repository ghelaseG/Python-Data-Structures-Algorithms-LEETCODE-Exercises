"""
Design an algorithm to encode a list of strings to a single string. The encoded string is then decoded back to the original list of strings.

Please implement encode and decode
"""
# from typing import List

# class Solution:

#     def encode(self, strs: List[str]) -> str:
#         if not strs:
#             return ""
        
#         sizes, res = [], ""
#         for s in strs:
#             sizes.append(len(s))
#         for sz in sizes:
#             res += str(sz)
#             res += ','
#         res += '#'
#         for s in strs:
#             res += s
#         return res


#     def decode(self, s: str) -> List[str]:

#         if not s:
#             return []
        
#         sizes, res, i = [], [], 0
#         while s[i] != '#':
#             cur = ""
#             while s[i] != ',':
#                 cur += s[i]
#                 i += 1
#             sizes.append(int(cur))
#             i += 1
#         i += 1
#         for sz in sizes:
#             res.append(s[i:i + sz])
#             i += sz
#         return res

# solution = Solution()

# strs = ["gg","does","love","you"]
# s = solution.encode(strs)

# print(s)

# r = solution.decode(s)

# print(r)


from typing import List

class Solution:

    def encode(self, strs: List[str]) -> str:
        result = ""
        for s in strs:
            result += str(len(s)) + "#" + s
        return result
    
    def decode(self, s: str) -> List[str]:
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

solution = Solution()

strs = ["gg","does","love","you"]
s = solution.encode(strs)

print(s)

r = solution.decode(s)

print(r)