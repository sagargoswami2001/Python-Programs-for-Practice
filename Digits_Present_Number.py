# Python Program to Count the Number of Digits Present In a Number.

# Method 1: Using While Loop
num = int(input("Enter a Number Here: "))
# num = 12345
count = 0
while num != 0:
    num = num // 10
    count = count + 1

print(count)


# Method 2: Using len() Function
num = int(input("Enter a Number Here: "))
# num = 12345
x = len(str(num))
print(x)