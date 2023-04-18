# Python Program to Find the Factorial of a Number.
# 1st Method (Using For Loop)
# num = int(input("Enter a Number Here: "))

# fact = 1

# if num < 0:
#     print("Factorial of 0 Does not Exist")
# if num == 0:
#     print("Factorial of 0 is", 1)
# if num > 0:
#     for i in range(1, num + 1):
#         fact = fact * i
# print("The Factorial of the Given Number is", fact)

# 2nd Method (Using Recursion)
def fact(a):
    if a == 0:
        return 1
    else:
        return ((a)*fact(a-1))

num = int(input("Enter a Number Here: "))
result = fact(num)
print("The Factorial of the Given Number is", result)