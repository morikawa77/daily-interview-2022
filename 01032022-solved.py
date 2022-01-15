# Hi, here's your problem today. This problem was recently asked by Facebook:

# Reshaping a matrix means to take the same elements in a matrix but change the row and column length. This means that the new matrix needs to have the same elements filled in the same row order as the old matrix. Given a matrix, a new row size x and a new column size y, reshape the matrix. If it is not possible to reshape, return None.

def reshape_matrix(mat, x, y):
    flat_list = [item for sublist in mat for item in sublist]

    matrix = [[] for i in range(y)]

    try: 
      for i in range(y):
          for j in range(x):
              matrix[i].append(flat_list[i * x + j])

      return matrix 

    except IndexError:
      return None



print(reshape_matrix([[1, 2], [3, 4]], 1, 4))
# [[1], [2], [3], [4]]

print(reshape_matrix([[1, 2], [3, 4]], 2, 3))
# None
