# Python Program to Display Powers of 2 Using Anonymous(Lambda) Function.

nterms = int(input("Enter Number of Terms Here: "))
result = list(map(lambda x : 2 ** x, range(nterms + 1)))
# print(result)

for i in range(nterms+1):
    print("The Value of 2 Raised to Power", i, "is", result[i])
