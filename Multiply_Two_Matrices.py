# Python Program to Multiply Two Matrices.
A = [[1,3,5],
     [7,9,11],
     [13,15,17]]

B = [[2,4,6,7],
     [8,10,12,9],
     [14,16,18,11]]

Result = [[0,0,0,0],
          [0,0,0,0],
          [0,0,0,0]]

for i in range(len(A)):
    for j in range(len(B[0])):
        for k in range(len(B)):
            Result[i][j] += A[i][k] * B[k][j]

for i in Result:
    print(i)
    