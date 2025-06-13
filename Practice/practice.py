# https://www.youtube.com/watch?v=nRkx4pOvMYI&list=PL3dZTJxh461hd5_Ho6pyEHvnCef3Sv3oU&ab_channel=KyleWilsonCode
# https://www.youtube.com/watch?v=0K_eZGS5NsU&t=10s&ab_channel=NeetCode
"""
recap python
"""

# Python 3 basics:

#splice, split() and join()

names = ["Todd", "Jake", "Bill", "Sally", "Anna", "Mikala"]

print(names[1:])

print(names[3:])

print(names[:2])

print(names[-2])

print(names[-3:])


ssn = "123-12-1234"

ssnList = ssn.split("-")
print(ssnList)

b = "Jake walks his dog"
print(b.split())

c = ['Jake', 'walks', 'his', 'dog']
" ".join(c)

print(",".join(c))



# if

#Ask for the user's age
print("Please enter your age")
age = input()
age = int(age)

#If they are older than 21, invite them in
if age > 21:
    print("Come in")
    print("Old friend")
#elif
#If they are 21, give them a free drink
#If they are younger than 21, tell them to go away
elif age == 21:
    print("Have a drink on the house")         

#else
else:
    print('You\'re not allowed in')

#Wish them goodnight
print("Good night")

#nested if statement
a = 5
b = 3
c = 4

if a > b:
    if a > c:
        print("A is the biggest")


#while loops
        

print("Day: 1")
print("Day: 2")

counter = 0
while counter < 5:
    print("Day: " + str(counter))
    counter += 1

#for loops
    
test_scores = [81, 85, 20, 68]
mySum = 0

for myNum in test_scores:
    mySum += myNum
print(mySum/len(test_scores))

#for loop using range

for number in range(0, 5, 2):
    print(number)

test_scores = [81, 85, 20, 68]
mySum = 0

for myNum in range(len(test_scores)):
    mySum += test_scores[myNum]
print(mySum/len(test_scores))



# functions

def say_name(name, age):
    print(name + " is " + str(age) + " years old.")

myName = "Scott"
say_name("George", 32)
say_name(myName, 42)


# return

def add_nums(num1, num2):
    mySum = num1 + num2
    return mySum

def double_num(num):
    doubled_num = num*2
    return doubled_num

calc_sum = add_nums(4,2)
dbl_num = double_num(calc_sum)
print(dbl_num)


#tuples

myTuple = ('student A', 99, True)
myList = ['student B', 85, True]

print(type(myTuple))
print(type(myList))

myList[1] = 95
print(myList)

myTuple[1] = 83
print(myTuple)


#break and continue

#find the first number greater than 5
myNums = [1,3,4,8,1,7]

for num in myNums:
    print(num)
    if num > 5:
        print(num)
        break

#add al positive numbers
myNums = [2,-5,2,-8,6,-1,9]
mySum = 0

for num in myNums:
    if num < 0:
        continue
    mySum += num
print(mySum)


#default and keyword arguments

def student(name, gpa = 4.0):
    print(name + ":" + str(gpa))

student("George")

# class and init

class Enemy():
    # attack = 20
    # health = 100

    def __init__(self, e_attack, e_health):
        print("An object was created")
        self.attack = e_attack
        self.health = e_health


    def enemy_attack(self):
        print("I'm attacking for " + str(self.attack) + " damage.")
    
    def enemy_damage(self):
        print("Ow")

ogre = Enemy(30, 200)
# print(ogre.attack)
print("--------------------")
ogre.enemy_attack()

orc = Enemy(40, 50)
orc.enemy_attack()

# lambda

arr = ["bob", "alice", "jane", "doe"]
arr.sort()
print(arr)

## Custom sort ( by length of string )
arr.sort(key = lambda x: len(x))
print(arr)

def my_map(my_func, my_iter):
    result = []
    for item in my_iter:
        new_item = my_func(item)
        result.append(new_item)
    return(result)

nums = [3, 4, 5, 6, 7]

cubed = my_map(lambda x: x**3, nums)

print(cubed)

# zip function
## loop through multiple arrays simultaneously with unpacking

nums1 = [1, 3, 5]
nums2 = [2, 4, 6]

for n1, n2 in zip(nums1, nums2):
    print(n1, n2)
