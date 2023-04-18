# Python Program to Check Armstrong Number.
num = int(input("Enter a Number: "))
order = len(str(num))

sum = 0
temp = num

while temp > 0:
    digit = temp % 10
    # sum += digit ** 3
    cube = digit ** order
    sum = sum + cube
    temp //= 10

if sum == num:
    print("It is an Armstrong Number")
else:
    print("It is not an Armstrong Number")
