import numpy as np

# flatten เปลี่ยนเป็น1-D ถ้าตัวหนึ่งเปลี่ยน อีกตัวหนึ่งไม่เปลี่ยน
a = np.array([[1,2],[3,4],[5,6]])
print(a)
print(a.flatten())
print(a)
b = a.flatten()
print(a)
print(b)
b[0] = 9    # เปลี่ยนแค่ b
print(b)
print(a)
print()

# ravel เปลี่ยนเป็น1-D ถ้าตัวหนึ่งเปลี่ยน อีกตัวหนึ่งเปลี่ยนด้วย
a = np.array([[7,8],[9,10],[11,12]])
print(a)
print(a.ravel())
print(a)
b = a.ravel()
print(b)
b[0] = 49
print(b)
print(a)
print()

# transpose เปลี่ยนแถวเป็นหลัก เปลี่ยนหลักเป็นแถว
a = np.array([[1,2,3],[4,5,6]])
print(a)
print(a.transpose())
print(a)
b = a.transpose()
print(b)
print(a.shape)
print(b.shape)
