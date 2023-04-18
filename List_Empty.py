# Python Program to Check if a List is Empty.

# Method 1 : Using Boolean Operation
my_list = []
if not my_list:
    print("The List is Empty")

# Method 2 : Using len() Function
my_list = [1,2,3,4,5]
print(len(my_list))
if len(my_list)==0:
    print("The List is Empty")

# Method 3 : Using []
my_list = [12,4,56,7]
if my_list == []:
    print("The List is Empty")
