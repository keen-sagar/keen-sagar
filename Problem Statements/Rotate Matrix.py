import numpy as np
mat1 = [[1,2,3],[4,5,6],[7,8,9]]
mat2 = [[7,4,1],[8,5,2],[9,6,3]]
print("Original Matrix")
for j in mat1:
    print(j)

#Transpose of matrix(rows swapped with columns)

def transpose(mat1):
    row = int(len(mat1))
    col = int(len(mat1[0]))
    mat2 = np.empty((row,col),int)
    for i in range(row):
        for j in range(col):
            mat2[i][j] = mat1[j][i]
    print("Transpose of Matrix")
    for j in mat2:
        print(j)
    rotate(mat2)

def rotate(mat):
    print("After Rotation")
    for i in range(len(mat)):
        for j in range(len(mat[0])-1,-1,-1):
            print(mat[i][j],end='')
        print("")

transpose(mat1)