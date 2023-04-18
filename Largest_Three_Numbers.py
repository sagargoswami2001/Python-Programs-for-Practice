# Python Program to Find the Largest Among Three Numbers.
num1 = int(input("Enter Number 1st Here: "))
num2 = int(input("Enter Number 2nd Here: "))
num3 = int(input("Enter Number 3rd Here: "))

if (num1 > num2) and (num1 > num3):
    print(num1, "is the Largest Number")

elif (num2 > num3) and (num2 > num1):
    print(num2, "is the Largest Number")

elif (num3 > num1) and (num3 > num2):
    print(num3, "is the Largest Number")

else:
    print("None")
