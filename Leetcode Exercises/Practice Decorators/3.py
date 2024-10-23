"""
Write a Python program to create a decorator to convert the return value of a function to a specified data type.
"""

def convert_to_data_type(data_type):
    def decorator(func):
        def wrapper(*args, **kwargs):
            result = func(*args, **kwargs)
            return data_type(result)
        return wrapper
    return decorator