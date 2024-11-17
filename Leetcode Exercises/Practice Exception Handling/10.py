"""
Write a Python program that executes a list operation and handles an AttributeError exception if the attribute does not exist.
"""

def list_operation(nums):
    try:
        operation = input("write an operation you want to be executed:")
        exec(operation)
        #resulty = len(nums)
        #print(type(resulty))
        #result = operation, nums
        #print(type(result))
        #result2 = result.join()
        #print(result2)
        #result3 = result2(nums)
        result = eval(f"{operation}({nums})")
        print("Operation result is:", result)
    except AttributeError:
        print("Error: the list does not have a 'length' attribute")

nums = [1, 2, 3, 4, 5, 6, 7, 8, 9]
list_operation(nums)

#nums2 = ('abc')
#list_operation(nums2)