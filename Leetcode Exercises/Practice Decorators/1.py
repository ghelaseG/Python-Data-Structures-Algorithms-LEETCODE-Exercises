"""
Write a Python program to create a decorator that logs the arguments and return value of a function.
"""

def decorator(func):
    def wrap(*args, **kwargs):
        #log the function name and arguments
        print(f"Calling {func.__name__} with args: {args}, kwargs: {kwargs}")

        #call the original function
        result = func(*args, **kwargs)

        #log the return value
        print(f"{func.__name__} returned: {result}")

        #return the result
        return result
    return wrap

