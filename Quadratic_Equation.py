# Python Program to Solve Quadratic Equation.

# Setisfy Conditions:
# Formula : ax**2 + bx + c = 0
# a, b and c are real numbers
# a!= 0

import cmath
a = int(input("Enter Number (a!=0): "))
b = int(input("Enter Number: "))
c = int(input("Enter Number: "))

# Formula for Discriminant
d = (b**2) - (4*a*c)

root1 = (-b-cmath.sqrt(d))/(2*a)
root2 = (-b+cmath.sqrt(d))/(2*a)

print("The Roots Are", root1, "&", root2)