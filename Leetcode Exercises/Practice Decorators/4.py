"""
Write a Python program that implements a decorator to cache the result of a function.
"""

def cache_result(func):
    cache = {}
    #we build this wrapper to add extra functionality to our main function
    def wrapper(*args, **kwargs):
        key = (*args, *kwargs.items())

        if key in cache:
            print("Retrieving result from cache ...")
            return cache[key]
        
        result = func(*args, **kwargs)
        cache[key] = result

        return result
    
    return wrapper

@cache_result
def calculate_multiply(x, y):
    print("Calculating the product of two numbers ...")
    return x * y

#Call the decorated function multiple times
print(calculate_multiply(4, 5))  # Calculation is performed
print(calculate_multiply(4, 5))  # Result is retrieved from cache
print(calculate_multiply(5, 7))  # Calculation is performed
print(calculate_multiply(5, 7))  # Result is retrieved from cache
print(calculate_multiply(-3, 7))  # Calculation is performed
print(calculate_multiply(-3, 7))  # Result is retrieved from cache

"""
!info: we need this cache function because of the repetitive operations, instead of doing the same thing 2 times or more times, we just retrieved from our cache.
"""