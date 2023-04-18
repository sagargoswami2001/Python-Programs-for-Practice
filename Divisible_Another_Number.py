# Python Program to Find Numbers Divisible by Another Number.
# 1st Method (Using For Loop & Conditional Statement)

# print("The Numbers Divisible By 13 Are: ")
# for i in range(1,100):
#     if i % 13 == 0:
#         print(i)
        

# 2nd Method (Using Lambda Function and filter())
li = [39,48,26,98,33,67,87]
result = list(filter(lambda x : x % 13 == 0,li))
print("The Numbers Divisible By 13 are: ", result)
