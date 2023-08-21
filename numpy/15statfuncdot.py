import numpy as np

# 1D array
a = np.array([1,2,3,4,5])
print(a)
print(a.sum())      # ผลรวม
print(a.prod())      # ผลคูณ
print(a.mean())      # ค่ามัธยฐาน
print(a.max())      # ค่ามากสุด
print(a.min())      # ค่าน้อยสุด
print(a.argmax())      # ตำแหน่งค่ามากสุด
print(a.argmin())      # ตำแหน่งค่าน้อยสุด
print()

# 2D array
# axis=0 --> col , axis=1 --> row
b = np.array([[10,20,30],[40,50,60],[70,80,90]])
print(b)
print(b.min())
print(np.min(b,axis=1))
print(b.max())
print(np.max(b,axis=0))
print()

# Dot Product (Matrix)
a = np.array([[1,2],[3,4]])
print(a)
b = np.array([[11,12],[13,14]])
print(b)
c = a.dot(b)
print(c)

