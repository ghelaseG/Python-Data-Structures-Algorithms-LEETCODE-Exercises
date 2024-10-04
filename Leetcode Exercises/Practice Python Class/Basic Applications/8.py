"""
Write a Python class to reverse a string word by word.
Input string : 'hello .py'
Expected Output : '.py hello'
"""

class Solution8:
    def reverse_words(self, word):
        return ' '.join(reversed(word.split()))

print(Solution8().reverse_words('hello .py'))