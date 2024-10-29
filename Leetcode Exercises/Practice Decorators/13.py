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


for param_name, annot in sig.parameters.items():
    print(f"Parameter '{param_name}' has annotation: {annot.annotation}")

#this will print what is after the arrow '-> float'
return_annotation = sig.return_annotation
print(f"The return type annotation is: {return_annotation}")
