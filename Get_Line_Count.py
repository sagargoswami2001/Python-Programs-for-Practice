# Python Program to Get Line Count of a File.

# Method 1: Using Len() Function
f = open("Get_Line_Count.txt", "r")
print(len(f.readlines()))
f.close()


# Method 2: Using List Comprehension
lines = sum(1 for i in open("Get_Line_Count.txt"))
print(lines)
