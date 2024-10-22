"""
Write a Python program to create a decorator function to measure the execution time of a function.
"""
import time

#let's create the decorator

def measure_execution_time(func):

    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        execution_time = end_time - start_time
        print(f"Function {func.__name__} took {execution_time:.4f} seconds to execute")
        return result
    return wrapper
