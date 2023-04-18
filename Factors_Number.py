# Python Program to Find the Factors of a Number.

num = int(input("Enter a Number Here: "))

for i in range(1, num+1):
    if num % i == 0:
        print(i)
        