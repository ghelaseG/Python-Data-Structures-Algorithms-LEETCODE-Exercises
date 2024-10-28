"""
Write a Python program that implements a decorator to provide caching with expiration time for a function.
"""
import time

def cache_with_expiry(expiry_time):
    def decorator(func):
        cache = {}
        def wrapper(*args, **kwargs):
            key = (*args, *kwargs.items())
            if key in cache:
                value, timestamp = cache[key]
                if time.time() - timestamp < expiry_time:
                    print("Retrieving result from cache ...")
                    return value
            result = func(*args, **kwargs)
            cache[key] = (result, time.time())
            return result
        return wrapper
    return decorator