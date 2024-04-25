"""
Check to see if a string of parentheses is balanced or not.

By "balanced," we mean that for every open parenthesis, there is a matching closing parenthesis in the correct order. For example, the string "((()))" has three pairs of balanced parentheses, so it is a balanced string. On the other hand, the string "(()))" has an imbalance, as the last two parentheses do not match, so it is not balanced.  Also, the string ")(" is not balanced because the close parenthesis needs to follow the open parenthesis.

Your program should take a string of parentheses as input and return True if it is balanced, or False if it is not. In order to solve this problem, use a Stack data structure.

Function name:
is_balanced_parentheses

Remember: this is not a method within the Stack class, this is a separate function.  Indent all the way to the left.
"""

class Stack:
    def __init__(self):
        self.stack_list = []

    def print_stack(self):
        for i in range(len(self.stack_list)-1, -1, -1):
            print(self.stack_list[i])

    def is_empty(self):
        return len(self.stack_list) == 0
    
    def peek(self):
        if self.is_empty():
            return None
        else:
            return self.stack_list[-1]
    
    def size(self):
        return len(self.stack_list)
    
    def push(self, value):
        self.stack_list.append(value)

    def pop(self):
        if self.is_empty():
            return None
        else:
            return self.stack_list.pop()
        

def is_balanced_parentheses(parantheses):
    stack = Stack()
    for i in parantheses:
        if i == '(':
            stack.push(i)
        elif i == ')':
            #here we check if the parentheses are (),
            #if not they will return false, so it will iterate again and again, until stack is empty
            if stack.is_empty() or stack.pop() != '(':
                return False
    return stack.is_empty() #if this condition is true, then the parantheses are balanced

"""
Big O:
Time complexity: 
- for loop : O(n)
- stack.push()/pop() : O(1)
- those together makes it O(n)
Space complexity:
- if the stack_list stores all the parantheses then it will make O(n)
"""

def test_is_balanced_parantheses():
    try:
        assert is_balanced_parentheses('((()))') == True
        print('Test case 1 passed')
    except AssertionError:
        print('Test case 1 failed')

    try:
        assert is_balanced_parentheses('()') == True
        print('Test case 2 passed')
    except AssertionError:
        print('Test case 2 failed')
    
    try:
        assert is_balanced_parentheses('(()())') == True
        print('Test case 3 passed')
    except AssertionError:
        print('Test case 3 failed')

    try:
        assert is_balanced_parentheses('(()') == False
        print('Test case 4 passed')
    except AssertionError:
        print('Test case 4 failed')

    try:
        assert is_balanced_parentheses('())') == False
        print('Test case 5 passed')
    except AssertionError:
        print('Test case 5 failed')
    
    try:
        assert is_balanced_parentheses(')(') == False
        print('Test case 6 passed')
    except AssertionError:
        print('Test case 6 failed')
    
    try:
        assert is_balanced_parentheses('') == False
        print('Test case 7 passed')
    except AssertionError:
        print('Test case 7 failed')

    try:
        assert is_balanced_parentheses('()()()()') == True
        print('test case 8 passed')
    except AssertionError:
        print('Test case 8 failed')

    try:
        assert is_balanced_parentheses('(())(())') == True
        print('Test case 9 passed')
    except AssertionError:
        print('Test case 9 failed')

    try:
        assert is_balanced_parentheses('(()()())') == True
        print('test case 10 passed')
    except AssertionError:
        print('Test case 10 failed')
    
    try:
        assert is_balanced_parentheses('((())') == False
        print('Test case 11 passed')
    except AssertionError:
        print('Test case 11 failed')

test_is_balanced_parantheses()