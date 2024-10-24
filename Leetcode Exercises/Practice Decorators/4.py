"""
Write a Python program that implements a decorator to cache the result of a function.
"""

def cache_result(func):
    cache = {}

    def wrapper(*args, **kwargs):
        key = (*args, *kwargs.items())

        if key in cache:
            print("Retrieving result from cache ...")
            return cache[key]
        
        result = func(*args, **kwargs)
        cache[key] = result

        return result
    
    return wrapper