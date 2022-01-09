# Hi, here's your problem today. This problem was recently asked by Facebook:

# Reshaping a matrix means to take the same elements in a matrix but change the row and column length. This means that the new matrix needs to have the same elements filled in the same row order as the old matrix. Given a matrix, a new row size x and a new column size y, reshape the matrix. If it is not possible to reshape, return None.

from functools import reduce 
from operator import mul

def reshape_matrix(mat, x, y):
    shape = [x, y]

    if len(shape) == 1:
        return mat

    n = reduce(mul, shape[1:])

    sizeArray = 0

    for i in range(len(mat)):
        sizeArray += len(mat[i])
        i+=1

    # if reduce(mul, shape) == len(mat):
    if x * y == sizeArray:
      return [reshape_matrix(mat[i*n:(i+1)*n], shape[1:]) for i in range(len(mat)//n)]

    else:
      return None





print(reshape_matrix([[1, 2], [3, 4]], 1, 4))
# [[1], [2], [3], [4]]

print(reshape_matrix([[1, 2], [3, 4]], 2, 3))
# None
