"""

Given two strings s and t, return true if the two strings are anagrams of each other, otherwise return false.

An anagram is a string that contains the exact same characters as another string, but the order of the characters can be different.
"""

class Solution:
    def valid_anag(self, s:str, t:str) -> bool:
    # part 1
    #    if len(s) != len(t):
    #       return False
        
    #    return sorted(s) == sorted(t)

    # part 2
        if len(s) != len(t):
            return False
        
        count_s = {}
        count_t = {}

        for i in range(len(s)):
            count_s[s[i]] = count_s.get(s[i], 0)
            count_t[t[i]] = count_t.get(t[i], 0)
        
        return count_s == count_t


s = "racecar"
t = "carrace"
solut = Solution()
print(solut.valid_anag(s, t))