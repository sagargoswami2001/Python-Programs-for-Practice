# Python Program to Check Whether a String is Palindrome or Not.

s = input("Enter a Word Here: ")
rev = s[::-1]

if s == rev:
    print("It is Palindrome")
else:
    print("It is not Palindrome")
