"""
Practice signature, annotation functions
"""

#this holds the signature module
from inspect import signature

#here we expect to get a float result
def add_num(x: int, y: float) -> float:
    return a + b

#signature prints the parameters of the function
sig = signature(add_num)
print(sig)
