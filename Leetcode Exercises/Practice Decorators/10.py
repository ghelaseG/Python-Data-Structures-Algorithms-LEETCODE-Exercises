"""
Write a Python program that implements a decorator to enforce type checking on the arguments of a function.
"""

import inspect

def enforce_type_checking(func):
    def wrapper(*args, **kwargs):
        #get the function signature and parameter names
        signature = inspect.signature(func)
        parameters = signature.parameters

        #iterate over the positional arguments
        for i, arg in enumerate(args):
            param_name = list(parameters.keys)[i]
            param_type = parameters[param_name].annotation
            if not isinstance(arg, param_type):
                raise TypeError(f"Argument '{param_name}' must be of type '{param_type.__name__}'")
            
        #iterate over the keyword arguments
        for param_name, arg in kwargs.items():
            param_type = parameters[param_name].annotation
            if not isinstance(arg, param_type):
                raise TypeError(f"Argument '{param_name}' must be of type '{param_type.__name__}'")
        
        #call the original function
        return func(*args, **kwargs)
    
    return wrapper
