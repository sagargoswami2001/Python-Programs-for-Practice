# Python Program to make a Simple Calculator.

print("----------Mini Calculator----------")

num1 = float(input("\nEnter fisrt Number Here: "))
num2 = float(input("Enter Second Number Here: "))

print("\nPress 1 for Addition \nPress 2 for Subtraction \nPress 3 for Multiplication \nPress 4 for Division")

choice = int(input("\nEnter Your Choice: "))
if choice == 1:
    print(num1 + num2)
elif choice == 2:
    print(num1 - num2)
elif choice == 3:
    print(num1 * num2)
elif choice == 4:
    print(num1 / num2)
else:
    print("Invalid Input")
