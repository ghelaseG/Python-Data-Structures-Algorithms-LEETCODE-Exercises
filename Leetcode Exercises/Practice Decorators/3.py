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

#examples
@convert_to_data_type(int)
def add_numbers(x, y):
    return x + y

result = add_numbers(10, 40)
print("Result:", result, type(result))


@convert_to_data_type(str)
def concatenate_str(x, y):
    return x + y

result = concatenate_str("Python", " Decorator")
print("Result:", result, type(result))