"""
Write a Python class to check the validity of a string of parentheses, '(', ')', '{', '}', '[' and ']. These brackets must be closed in the correct order, for example "()" and "()[]{}" are valid but "[)", "({[)]" and "{{{" are invalid.
"""

class Solution3:
    def check_paranthese(self, parantheses):
        stack, parantheses_char = [], {"(": ")", "{": "}", "[": "]"}
        for i in parantheses:
            if i in parantheses_char:
                stack.append(i)
            elif len(stack) == 0 or parantheses_char[stack.pop()] != i:
                return False
        return len(stack) == 0

print(Solution3().check_paranthese("(){}[]"))
print(Solution3().check_paranthese("()[{)}"))
print(Solution3().check_paranthese("()"))
