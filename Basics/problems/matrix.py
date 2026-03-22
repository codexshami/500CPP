import numpy as np
# 1- Mutiply two matrices
a= np.array([[1, 2], [3, 4]])
b = np.array([[5, 6], [7, 8]])  
c = np.dot(a, b)
print("Multiplication of two matrices:\n", c)
#2nd method
c = a @ b # this is used in only python 3.5 and above
print("Multiplication of two matrices using @ operator:\n", c)

#2 - Transpose of a matrix
d = np.transpose(a)
print("Transpose of matrix a:\n", d)

#3 - Inverse of a matrix
try:
    e = np.linalg.inv(a)
    print("Inverse of matrix a:\n", e)
except np.linalg.LinAlgError:
    print("Matrix a is singular and cannot be inverted.")

#4 - check if a matrix is symmetric
def is_symmetric(matrix):
    return np.array_equal(matrix, matrix.T) 
symmetric_matrix = np.array([[1, 2, 3], [2, 4, 5], [3, 5, 6]])
if is_symmetric(symmetric_matrix):
    print("Matrix is symmetric.")
else:
    print("Matrix is not symmetric.")

# 5 - find the sum of diagonal elements of a matrix
def sum_of_diagonal(matrix):
    return np.trace(matrix) 
matrix = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print("Sum of diagonal elements of the matrix:", sum_of_diagonal(matrix))

#6 - Rotate a matrix 90 degrees clockwise
def rotate_matrix_90_clockwise(matrix):
    return np.rot90(matrix, -1)  # -1 for clockwise rotation        
matrix_to_rotate = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])  
rotated_matrix = rotate_matrix_90_clockwise(matrix_to_rotate)
print("Matrix rotated 90 degrees clockwise:\n", rotated_matrix)

#7 - find the determinant of a matrix
def determinant_of_matrix(matrix):
    return np.linalg.det(matrix)    
matrix_for_determinant = np.array([[1, 2], [3, 4]])
det = determinant_of_matrix(matrix_for_determinant)
print("Determinant of the matrix:\n", det)

#8 -Print a matrix spiral order
def spiral_order(matrix):
    # Placeholder implementation
    pass
matrix_for_spiral = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
# Placeholder for spiral order function
print("Spiral order of the matrix:\n", spiral_order(matrix_for_spiral))

#9 - Find the number of iceland in a binary matrix
def count_islands(matrix):
    # Placeholder implementation
    pass    
matrix_for_islands = np.array([[1, 0, 1], [0, 1, 0], [1, 0, 1]])
# Placeholder for count islands function
print("Number of islands in the binary matrix:", count_islands(matrix_for_islands))

#10 - find the maximum sum of a submatrix
def max_sum_submatrix(matrix):
    # Placeholder implementation
    pass
matrix_for_max_sum = np.array([[1, -2, 3], [-4, 5, -6], [7, 8, -9]])
# Placeholder for max sum submatrix function
print("Maximum sum of a submatrix:", max_sum_submatrix(matrix_for_max_sum))