# Big O:
"""
Using memoization, we bring the fibonacci sequence from a time complexity of O(2^n) to O(n)
"""

memo = [None] * 100
counter = 0

def fib(n):
    global counter
    counter += 1

    if memo[n] is not None:
        return memo[n]
    
    if n == 0 or n == 1:
        return n
    
    memo[n] = fib(n-1) + fib(n-2)

    return memo[n]


n = 35

print('Fib of', n, '=', fib(n))
print('Counter:', counter) #O(2n -1)