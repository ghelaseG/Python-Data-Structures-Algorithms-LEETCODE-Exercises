"""
Write a Python program that implements a decorator to validate function arguments based on a given condition.
"""


def validate_arguments(condition):
    def decorator(func):
        