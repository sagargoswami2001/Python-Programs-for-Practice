# Python Program to Display the Multiplication Table.
# 1st Method (Using For Loop)
# num = int(input("Enter the Number: "))
# for i in range(1, 11):
#     print(num, "X", i, "=", num*i)

# 2nd Method (Using While Loop)
num = int(input("Enter the Number: "))
i = 1
while i <= 10:
    print(num, "X", i, "=", num*i)
    # i = i+1
    i += 1
    