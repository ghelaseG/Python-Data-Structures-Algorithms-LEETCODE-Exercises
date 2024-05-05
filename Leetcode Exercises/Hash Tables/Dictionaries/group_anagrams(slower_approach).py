"""
You have been given an array of strings, where each string may contain only lowercase English letters. You need to write a function group_anagrams(strings) that groups the anagrams in the array together using a hash table (dictionary). The function should return a list of lists, where each inner list contains a group of anagrams.

For example, if the input array is ["eat", "tea", "tan", "ate", "nat", "bat"], the function should return [["eat","tea","ate"],["tan","nat"],["bat"]] because the first three strings are anagrams of each other, the next two strings are anagrams of each other, and the last string has no anagrams in the input array.

You need to implement the group_anagrams(strings) function and return a list of lists, where each inner list contains a group of anagrams according to the above requirements.
"""

# Time complexity of: O(n * k log k)

def group_anagrams(letters):
    #we create an empty hash table
    my_dict = {}

    for letter in letters:
        #we sort each string to get its canonical form (exp: eat -> a , e , t)
        #.join converts the array of characters to for exp "aet" strings
        canonical = ''.join(sorted(letter))

        #we then check to see if the canonical form of the string exists in the hash table
        if canonical in my_dict:
            #if it does then we add the string there
            my_dict[canonical].append(letter)
        else:
            #otherwise craete new canonical form and add the string there
            my_dict[canonical] = [letter]

    #convert the hash table to a list of lists
    return list(my_dict.values())
    
print("1st set:")
print( group_anagrams(["eat", "tea", "tan", "ate", "nat", "bat"]))

print("\n2nd set:")
print( group_anagrams(["abc", "cba", "bac", "foo", "bar"]))

print("\n3rd set:")
print( group_anagrams(["listen", "silent", "triangle", "integral", "garden", "ranged"]))