# Python Program to Find Factorial of Number Using Recursion.
def fact(n):
    if n == 1:
        return 1
    else:
        return (n * fact(n-1))

n = int(input("Enter a Number Here: "))
if n <= 0:
    print("Factorial of Number Less than 1 Does Not Exists")
else:
    print("Factorial of Given Number is", fact(n))
