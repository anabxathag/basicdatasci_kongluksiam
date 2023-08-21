import numpy as np

a = np.arange(1,11)
print(a)
print(np.delete(a,2))   # (a, index)
print(a)
print()
a = np.arange(1,13).reshape(4,3)
print(a)
print(np.delete(a,2,axis=0))    # romove row
print(np.delete(a,2,axis=1))    # romove col
print()
a = np.arange(1,21)
print(a)
print(np.split(a,4))    # แบ่งเป็น4ส่วน
print(np.split(a,5))    # แบ่งเป็น5ส่วน
print()
a = a.reshape(5,4)
print(a)
print(np.hsplit(a,4))    # แบ่งตามcol
print(np.hsplit(a,2))
print(np.vsplit(a,5))    # แบ่งตามrow
