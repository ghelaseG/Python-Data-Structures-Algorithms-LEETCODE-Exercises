"""
Write a Python program that implements a decorator to enforce rate limits on a function.
"""

import time

def rate_time_limits(max_calls, period):
    
    def decorator(func):
        calls = 0 
        last_reset = time.time()

        def wrapper(*args, **kwargs):
            nonlocal calls, last_reset

            elapsed = time.time() - last_reset

            if elapsed > period:
                calls = 0
                last_reset = time.time()

            if calls >= max_calls:
                raise Exception("Rate limit exceeded. Try again !!")
            
            calls += 1

            return func(*args, **kwargs)
        
        return wrapper
    return decorator
