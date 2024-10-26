"""
Write a Python program that implements a decorator to add logging functionality to a function.
"""

"""
Logging functionality refers to the capability of recording and storing information about program execution. It allows you to capture significant events, messages, and errors that occur during code execution.
"""

def logging_info(func):
    def wrapper(*args, **kwargs):
        #log the func name and arguments
        print(f"Calling {func.__name__} with args: {args}, kwargs: {kwargs}")

        result = func(*args, **kwargs)

        #log the return value
        print(f"{func.__name__} returned: {result}")

        return result
    return wrapper

@logging_info
def add_num(x, y):
    return x + y

#call the decorated function
result = add_num(100, 150)
print("Result:", result)