import numpy as np

b = np.array([[1,2,3],[4,5,6],[7,8,9]])
print(b.dtype)  # ชนิดข้อมูล
print(b.itemsize)   # มีกี่byte? (1 byte = 8 bit)
print(b.ndim)   # ขนาดมิติ
print(b.shape)  # ขนาด dept, row, col
b = np.array([[1,2,3],[4,5,6],[7,8,9],[10,11,12]])
print(b.shape)
print(b.size)   # จำนวนสมาชิก
print(b.itemsize)   # 32/8 = 4 byte
b = np.array([[1,2,3],[4,5,6],[7,8,9]], dtype="complex")
print(b.dtype)
print(b.itemsize)   # 128/8 = 16 byte
