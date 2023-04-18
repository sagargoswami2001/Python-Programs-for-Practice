# Python Program to Reverse a Number.

# Method 1: Using While Loop
num = int(input("Enter a Number Here: "))
reverse_num = 0
while num != 0:
    digit = num % 10
    reverse_num = reverse_num * 10 + digit
    num = num // 10
print("The Reverse of the Given Number is", reverse_num)


# Method 2: Using String Slicing
num = int(input("Enter a Number Here: "))
print("The Reverse of the Given Number is", str(num)[::-1])
