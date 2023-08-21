import numpy as np

a = np.array([3,4,2,6])
print(a)
b = np.array([8,7,5,10])
print(b)
c = np.concatenate((a,b))   # ต่อarrayกัน
print(c)
print()

print(np.append(a,100))     # เพิ่มสมาชิก
print(a)
a = np.append(a,500)
print(a)
print(np.insert(a,1,100))     # เพิ่มสมาชิกในตำแหน่งที่ต้องการ
print(np.insert(a,(1,3),100))       # เพิ่มหลายตำแหน่ง
print(np.insert(a,(1,3),(100,200)))
print()
b = np.array([[1,2],[3,4]])
print(b)
print(np.append(b,[[10],[20]],axis=1))  # row
# print(np.append(b,[[10],[20]],axis=0))  # col ==> error
print(np.insert(b,1,100,axis=0))
print(np.insert(b,1,50,axis=1))
print(np.insert(b,1,[10,20],axis=0))
print(np.insert(b,1,[10,20],axis=1))
