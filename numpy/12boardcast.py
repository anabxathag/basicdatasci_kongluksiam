import numpy as np
"""
# Board Casting
    - ขนาดมิติของ Array 2 ตัวไม่สอดคล้องกัน
"""
x = np.array([[1,2],[3,4],[5,6]])
y = np.array([10,20])     # boardcast ==> y = np.array([[10,20],[10,20],[10,20]])
print(x + y)
"""
ทำงานได้โดย boardcast array ที่มีขนาดเล็กกว่าถูกทำซ้ำ
เช่น array y มีขนาด 1 มิติ จะถูก boardcast ไปเป็น array 2มิติ
เพื่อให้สอดคล้องกับ array x เทียบมิติจากขวาไปซ้าย
"""
x = np.array([[1,2],[3,4],[5,6]])
y = np.array([2])     # boardcast ==> y = np.array([2,2],[2,2],[2,2])
print(x + y)
