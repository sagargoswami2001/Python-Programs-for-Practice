# Python Program to Compute the Power of a Number.

# Method 1: Using While Loop
base = int(input("Enter the Base Number: "))
exponent = int(input("Enter the Exponent: "))

result = 1
while exponent != 0:
    result = result * base
    exponent = exponent-1

print("The Computed Value is", result)


# Method 2: Using For Loop
base = int(input("Enter the Base Number: "))
exponent = int(input("Enter the Exponent: "))

result = 1
for i in range(exponent, 0,-1):
    result = result * base

print("The Computed Value is: ", result)


# Method 3: Using Power() Function
base = int(input("Enter Base Here: "))
exp = int(input("Enter Exponent Here: "))

x = pow(base, exp)
print("The Computed Value is: ", x)


# Method 4: Using Exponentiaition Operator
base = int(input("Enter Base Here: "))
exp = int(input("Enter Exponent Here: "))

value = base ** exp
print("The Computed Value is: ", value)
