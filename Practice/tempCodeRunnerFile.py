arr = ["bob", "alice", "jane", "doe"]
arr.sort()
print(arr)

## Custom sort ( by length of string )
arr.sort(key = lambda x: len(x))
print(arr)