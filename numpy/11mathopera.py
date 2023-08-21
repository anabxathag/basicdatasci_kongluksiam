import numpy as np

print("*1D_ARRAY*")
a = np.arange(1,5)
print(a)
print(a.shape)
print(a + 2)
print(a - 5)
print(a * 10)
print(a / 3)
print(a // 2)
print(a % 2)
print(a ** 3)
print()

b = np.arange(5,9)
print(b)
print(b.shape)
print(a + b)    # col ต้องเท่ากัน
print()

c = np.arange(1,11)
print(c)
print(c.shape)
print()

print("**2D_ARRAY**")
a = np.array([[1,2,3],[4,5,6]])
b = np.array([[7,8,9],[10,11,12]])
print(a)
print(a.shape)
print(b)
print(b.shape)
print()

print(a + b)    # row&col ต้องเท่ากัน
print(a - b)
print(a * b)
print(a / b)
print(a ** b)
print(a % b)
print(a + [2])  # +2 ในสมาชิกทุกตัว
print()

c = np.array([1,2,3])
print(c)
print(c.shape)
print(a + c)   # [+1,+2,+3] ในทุกๆrow ==> board casting
