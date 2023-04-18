# Python Program to Parse a String to a Float or Int.

# Method 1: Parse String Into Integer
string1 = '12345'
print(string1)
print(type(string1))
int_str = int(string1)
print(int_str)
print(type(int_str))


# Method 2: Parse String Into Float
string2 = "27.06"
print(string2)
print(type(string2))
float_str = float(string2)
print(float_str)
print(type(float_str))


# Method 3: Parse String Float Numeral Into Integer
string3 = "27.2001"
print(string3)
print(type(string3))
float_str = int(float(string3))
print(type(float_str))
