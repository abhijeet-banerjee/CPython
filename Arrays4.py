from numpy import *

m,n = [int(x) for x in input('Please enter row and then column followed by a space\n').split(',')]
s = input('Enter the nos. as in array\n').split(' ')
ar = matrix(reshape(s, (m, n)))
print(ar)

# finding the max and min elements
ar1 = [1,2,3,4,5]
print('Maximum element in the array %d and the minimum element in array %d' %(max(ar1),min(ar1)))

# create 2D Matrix

mat1 = [
    [1,2,3],
    [4,5,6],
    [7,8,9]
]

#print matrix 1 of 2D dimension
print(mat1)

# Add two 2D matrices
mat2 = [
    [1,2,3],
    [4,5,6],
    [7,8,9]
]
'''
Vectorized Operations On Matrix
'''
mat3 = matrix(mat1)+matrix(mat2)
print(mat3)

# finding Transpose of the Matrix

print('Now getting the transpose of Matrix mat3')
print(mat3.getT())
print(matrix(mat3)*3)
