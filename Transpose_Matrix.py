# Python Program to Transpose a Matrix.

# Method 1: Using For Loop
# A = [[1,3,5],
#      [7,9,11]]

# T = [[0,0],
#      [0,0],
#      [0,0]]

# for i in range(len(A)):
#     for j in range(len(A[0])):
#         T[j][i] = A[i][j]

# for i in T:
#     print(i)

# Method 2: Using List Comprehension
A = [[1,3,5],
     [7,9,11]]

T = [[A[j][i] for j in range(len(A))] for i in range(len(A[0]))]
for i in T:
    print(i)
