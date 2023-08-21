import numpy as np
# [start : stop : step]

# 1-D Arrays
a = np.arange(1,11)
print(a)
print(a[2])     
print(a[:])
print(a[7:])
print(a[:6])
print(a[3:8])
print(a[-8:-3])
print(a[2:9:2])
print(a[8:1:-2])

print()
# 2-D Arrays ==> [row, col]
x = np.array([[1,2,3],[4,5,6],[7,8,9]])
print(x[:, :])
print(x[1:, 1:])
print(x[2:, 2:])
print(x[:, 2:])
print(x[1, :])
print(x[:2, 1:])
print(x[1:2, 1:2])
print(x[::2, ::-1])
