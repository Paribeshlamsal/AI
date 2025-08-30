import numpy as np
matrixA=np.array([[1,2],[3,4]])
matrixB=np.array([[5,6],[7,8]])
mul=np.dot(matrixA,matrixB)
print(mul)
mul1=matrixA*matrixB
print(mul1)
transpose=matrixA.T
print(transpose)
det=np.linalg.det(matrixB)
print(det)
inv=np.linalg.inv(matrixB)
print(inv)