# Python Program to Display Fibonacci Sequence Using Recursion.
def fibo (n):
    if n <= 1:
        return n
    else:
        return fibo(n-1)+fibo(n-2)

n = int(input("Enter a Number Here: "))
if n <= 0:
    print("Enter a Positive Number")
else:
    print("Fibonacci Sequence")
    for i in range(n):
        print(fibo(i))
        