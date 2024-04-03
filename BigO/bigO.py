# O(n) - Proportional

def print_items(n):
    for i in range(n):
        print(i)
#Simplification Technique: Drop Constants or n + n or O(2n) which is O(n)
    for j in range(n):
        print(j)

print_items(10)


# O(n²) - Loop within a loop

def print_items(n):
    for i in range(n):
        for j in range(n):
            print(i,j)
#Simplification Technique: Drop Non-Dominants or # O(n²+n) - n being dropped as we keep - n² dominant term
    for k in range(n):
        print(k)

print_items(10)


# O(1) - the most efficient big O - constant time (as it increases, the number of operations remain constant)

def add_items(n):
    return n + n


# O(log n) - we use it to cut numbers in half as it is more faster.
## O(log n) - Divide and Conquer
# O(nlog n) - it is used with some sorting algorithms - merge sort or quick sort.


#Different Terms for Inputs

def print_items(a, b):
    for i in range(a):
        print(i)
    for j in range(b):
        print(j)
#here we're going to have O(a+b)
#and for nested for loops we have O(a*b) 
def print_items(a,b):
    for i in range(a):
        for j in range(b):
            print(i, j)

# Big O of Lists - if we add or remove at the beginning of the list is O(n) and at the end is O(1)