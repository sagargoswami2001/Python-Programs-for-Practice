# Python Program to Check Prime Number.
num = int(input("Enter a Number Here: "))
if num == 1:
    print("It is not a Prime Number")
if num > 1:
    for i in range(2, num):
        if num % i == 0:
            print("It is Not a Prime Number")
            break
    else:
        print("It is a Prime Number")
