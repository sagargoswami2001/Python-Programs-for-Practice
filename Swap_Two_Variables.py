# Python Program to Swap Two Variables.
# 1st Method (Using Third Variable)
# x = 27
# y = 9
# temp = x
# x = y
# y = temp
# print(x)
# print(y)

# 2nd Method (Without Using Third Variable)
x = 27
y = 9

x, y = y, x
print("The Value of X is: ", x)
print("The Value of Y is: ", y)
