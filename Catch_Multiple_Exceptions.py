# Python Program to Catch Multiple Exceptions in One Line.

# Method 1: Handling Multiple Exceptions
string = input("Enter Something Here: ")

try:
    num = int(input("Enter a Number Here: "))
    print(string + num)
except (ValueError,TypeError) as a:
    print(a)
    