# Python Program to Remove Duplicate Element From a List.

# Method 1: Using Set Datatype
l = [2,4,6,8,10,8,6,4,2]
x = list(set(l))
print(x)
print(type(x))


# Method 2
S = [2,4,6,8,10,8,6,4,2]
M = [10,12,14,16,18,20]
print(list(set(S)^set(M)))
