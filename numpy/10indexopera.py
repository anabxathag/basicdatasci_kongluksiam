import numpy as np

x = np.arange(1,10)
print(x)
index = np.array([1,5,7])
print(index)
print(x[index])
print(x[[1,5,7]])   # [[col_1,col_2,col_3]]
print(x[2])         # [col]
print(x[[2,5,2,5,2,5,2,5]])
index = np.array([2,4,6,8])
print(index)
print(x[index])
print()

b = np.array([[1,2,3],[4,5,6],[7,8,9]])
print(b)
print(b[0,2])           # [row,col]
print(b[[0,2]])         # [[row_1,row_2]]
print(b[[0,2],[2,0]])   # [[row_1,row_2],[col_1,col_2]]
print(b[[0,2],[1]])   # [[row_1,row_2],[col]]
print(b[[1],[0,1]])   # [[row],[col_1,col_2]]
print()

x = np.array([[1,-2,3],[4,-5,-6]])
print(x)
print(x[x < 0])         # boolean
print(x[x < 0] * -10)
print(x[x < 0] ** 2)
print(x[x > 0])

