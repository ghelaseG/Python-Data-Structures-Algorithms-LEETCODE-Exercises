# we got 2 lists, we need to check if we have any item in common

#space complexity O(n^2) - inefficient
def item_in_common(list1, list2):
    for i in list1:
        for j in list2:
            if i == j:
                return True
    return False

list1 = [1, 3, 5]
list2 = [2, 4, 5]

print(item_in_common(list1, list2))