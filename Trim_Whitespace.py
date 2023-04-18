# Python Program to Trim Whitespace from a String.

# Method 1: Using Strip() Function
string = " I Love Python "
strings = " \nI Love Python "
print(string)
print(string.strip())
print(string.strip(" "))


# Method 2: Using Regular Expression (Regex)
import re

string = "    I Love Python    "
x = re.sub(r'^\s+|\s+$','',string)
x = re.sub(r'^\s|\s$','',string)
print(x)
