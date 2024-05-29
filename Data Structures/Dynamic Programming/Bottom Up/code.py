counter = 0

def fib(n):
    fib_list = [0,1]
    global counter
    for index in range(2, n+1):
        counter += 1
        next_fib = fib_list[index - 1] + fib_list[index - 2]
        fib_list.append(next_fib)
    return fib_list[n]

n = 35

print('Fib of', n, '=', fib(n))
print('Counter:', counter)

"""
if we use memoization, the time complexity for the first run will be O(n),
and at the second run will be O(1). But, that means that it will take more memory.
"""