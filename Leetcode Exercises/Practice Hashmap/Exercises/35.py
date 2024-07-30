"""
Write a Python program to sort Counter by value.
Sample data : {'Math':81, 'Physics':83, 'Chemistry':87}
Expected data: [('Chemistry', 87), ('Physics', 83), ('Math', 81)]
"""

from collections import Counter

x = Counter({'Math': 81, 'Physics': 83, 'Chemistry': 87})

#print the most common elements which are subject-scores pairs

print(x.most_common())