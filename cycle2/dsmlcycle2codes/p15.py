import numpy as np

A =np.array( [[12, 7, 3],[4, 5, 6],[7, 8, 9]])
print("Matrix A:\n ",A)
B = np.array([[5, 8, 1, 2],[6, 7, 3, 0],[4, 5, 9, 1]])
print("Matrix B:\n ",B)
C = np.array([[1, 7, 3],[3, 5, 6],[6, 8, 9],[2, 9, 1]])
print("Matrix C:\n ",C)
result=np.dot(A,B)
#print(result)
new=np.dot(result,C)
print("Products of 3 mtrices is: \n", new)
#print(np.dot(np.dot(A,B),C))