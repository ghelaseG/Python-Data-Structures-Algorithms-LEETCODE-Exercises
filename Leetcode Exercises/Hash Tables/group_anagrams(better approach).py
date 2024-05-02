"""
You have been given an array of strings, where each string may contain only lowercase English letters. You need to write a function group_anagrams(strings) that groups the anagrams in the array together using a hash table (dictionary). The function should return a list of lists, where each inner list contains a group of anagrams.

For example, if the input array is ["eat", "tea", "tan", "ate", "nat", "bat"], the function should return [["eat","tea","ate"],["tan","nat"],["bat"]] because the first three strings are anagrams of each other, the next two strings are anagrams of each other, and the last string has no anagrams in the input array.

You need to implement the group_anagrams(strings) function and return a list of lists, where each inner list contains a group of anagrams according to the above requirements.
"""
# This is using a time and space complexity of O(m * n)/ O(n)

from collections import defaultdict

def group_anagrams(letters):
    my_dict = defaultdict(list)

    for letter in letters:
        lst = [0] * 26
        for char in letter:
            lst[ord(char) - ord('a')] += 1
        lst = tuple(lst)
        my_dict[lst].append(char)
    return my_dict.values()

    
print("1st set:")
print( group_anagrams(["eat", "tea", "tan", "ate", "nat", "bat"]))

print("\n2nd set:")
print( group_anagrams(["abc", "cba", "bac", "foo", "bar"]))

print("\n3rd set:")
print( group_anagrams(["listen", "silent", "triangle", "integral", "garden", "ranged"]))