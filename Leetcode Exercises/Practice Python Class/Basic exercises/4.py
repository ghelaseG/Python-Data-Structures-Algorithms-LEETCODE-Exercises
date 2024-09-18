"""
'builtins' module provides direct access to all 'built-in' identifiers of Python.
Write a Python program that imports the abs() function using the builtins module, displays the documentation of the abs() function and finds the absolute value of -155.
"""

import builtins

help(builtins.abs)

input_a = int(input('Write a negative number:'))
transforms = builtins.abs(input_a)
print(f'Absolute value of {input_a} is: {transforms}' )
