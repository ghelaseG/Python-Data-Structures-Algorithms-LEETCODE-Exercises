dic1 = {
    'value': 11
}

dic2 = dic1

print("Before value is updated:")
print("dic1 =", dic1)
print("dic2 =", dic2)

print("\ndic1 points to:", id(dic1))
print("dic2 points to:", id(dic2))

dic2['value'] = 22

print("\nAfter value is updated:")
print("dic1 =", dic1)
print("dic2 =", dic2)

print("\ndic1 points to:", id(dic1))
print("dic2 points to:", id(dic2))