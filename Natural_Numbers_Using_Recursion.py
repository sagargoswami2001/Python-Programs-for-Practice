# Python Program to Find Sum of Natural Numbers Using Recursion.
def Natural_Number_Sum (n):
    if n <= 1:
        return n
    else:
        return (n)+Natural_Number_Sum(n-1)

n = int(input("Enter a Number Here: "))
if n <= 0:
    print("Enter a Positive Number: ")
else:
    print("The Sum of Natural Number Upto Given Number is", Natural_Number_Sum(n))
    