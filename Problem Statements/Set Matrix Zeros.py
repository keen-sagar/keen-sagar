'''Problem Statement: Given a matrix if an element in the matrix is 0,
then you will have to set its entire column and row to 0 and then return the matrix.
'''
import numpy as np


def smz(matrix):
    row = int(len(matrix))
    col = int(len(matrix[0]))
    for i in range(row):
        for j in range(col):
            if matrix[i][j] == 0:
                for r in range(row):
                    if matrix[r][j] != 0:
                        matrix[r][j] = -1
                for c in range(col):
                    if matrix[i][c] != 0:
                        matrix[i][c] = -1

    for i in range(row):
        for j in range(col):
            if matrix[i][j] == -1:
                matrix[i][j] = 0
    return matrix



n = int(input("No. of Matrix: "))

for times in range(n):
    r,c = input(f"Size of matrix {times+1}: ").split()
    r,c = int(r), int(c)

    matrix = np.empty((r,c),int)
    for i in range(r):
        for j in range(c):
            element = int(input(f"Enter the [{i}][{j}] element of Matrix: "))
            matrix[i][j] = element
    print("Matrix Before:")
    for m in matrix:
        print(m)
    result = smz(matrix)
    print("Matrix After: ")
    for p in result:
        print(p)
