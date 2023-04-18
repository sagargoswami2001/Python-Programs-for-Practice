# Python Program to Concatenate Two Lists.

# Method 1: Using + Operator
List1 = [3,6,9,"S","G"]
List2 = [2,4,6,"M","G"]
List3 = List1 + List2
print(List3)


# Method 2: Using Unique Values
List1 = [3,6,9,"S","G"]
List2 = [2,4,6,"M","G"]
# List3 = {2,4,6,8,10,8,6,4,2}
List3 = list(set(List1 + List2))
print(List3)


# Method 3: Using Extend() Function
List1 = [3,6,9,"S","G"]
List2 = [2,4,6,"M","G"]
List1.extend(List2)
print(List1)
