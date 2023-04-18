# Python Program to Delete An Element From a Dictionary.

# Method 1: Using Delete Statement
marks = {"Sagar":97,"Mohit":95,"Prakash":99,"Goswami":93}
print(marks)
del marks["Prakash"]
print(marks)


# Method 2: Using pop() Function
marks = {"Sagar":97,"Mohit":95,"Prakash":99,"Goswami":93}
pop_item = marks.pop("Prakash")
print(marks)
