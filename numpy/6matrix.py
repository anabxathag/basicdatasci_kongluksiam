# Matrix คือ Array 2-di
# เมตริกซ์จัตุรัส(Square Matrix) = จำนวนrow&columnเท่ากัน
# เมตริกซ์ศูนย์(Zero Matrix) = สมาชิกทุกตัวเป็น0
# เมตริกซ์เอกลักษณ์(Identity Matrix) = สมาชิกเส้นทแยงมุมมีค่าเป็น1ที่เหลือ0

import numpy as np

# Zero Matrix
abc = np.zeros(5) # column
print(abc)
abc = np.zeros((2,2), dtype="int") # (row, column)
print(abc)
abc = np.zeros([3,4]) # [row, column]
print(abc)
print()

# Ones Matrix = สมาชิกทุกตัวเป็น1
abc = np.ones(5) # column
print(abc)
abc = np.ones((2,2), dtype="int") # (row, column)
print(abc)
abc = np.ones([4,3]) # [row, column]
print(abc)
print()

# Full Matrix(เมตริกซ์ค่าคงที่) = สมาชิกเหมือนกันทุกตัว
abc = np.full(5, 8) # column, เลขที่ต้องการ
print(abc)
abc = np.full((3,2), 6) # (row, column), เลขที่ต้องการ
print(abc)
print()

# Empty Matrix = สุ่มสมาชิกแต่ละทุกตัว
abc = np.empty((3,2)) # (row, column)
print(abc)
abc = np.empty([2,4]) # [row, column]
print(abc)
print()

# Identity Matrix
abc = np.identity(3) # dimention
print(abc)
abc = np.identity(2, dtype="int") # dimention
print(abc)
abc = np.eye(3) # dimention
print(abc)
abc = np.eye(3,5) # row, column
print(abc)
abc = np.eye(3,5,k=2) # ขยับไปทางขวา 2 col
print(abc)
abc = np.eye(3,5,k=-1) # ขยับไปทางซ้าย 1 col
print(abc)
