"""
Write a Python program to create a calculator class. Include methods for basic arithmetic operations
"""

class Calculator:

    def add(self, x, y):
        return x + y
    
    def subtract(self, x, y):
        return x - y
    
    def multiply(self, x, y):
        return x * y
    
    def divide(self, x, y):
        if y != 0:
            return x / y
        else:
            return ("Cannot divide by zero.")
        

calculator = Calculator()

result = calculator.add(7, 5)
print("7 + 5 =", result)

result = calculator.divide(0, 22)
print("0 / 22 =", result)

result = calculator.divide(22, 0)
print("22 / 0 =", result)