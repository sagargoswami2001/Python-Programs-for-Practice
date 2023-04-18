# Python Program to Merge Two Dictionaries.

# Method 1 : Using | Operator
dict1 = {"Sagar":89, "Mohit":99}
dict2 = {"Prakash":65, "Sagar":75}

print(dict1 | dict2)

# Method 2 : Using ** Operator
dict1 = {"Sagar":89, "Mohit":99}
dict2 = {"Prakash":65, "Sagar":75}

print({**dict1,**dict2})

# Method 3 : Using Copy() and Update() Methods
dict1 = {"Sagar":89, "Mohit":99}
dict2 = {"Prakash":65, "Sagar":75}

dict3 = dict2.copy()
dict3.update(dict1)
print(dict3)
