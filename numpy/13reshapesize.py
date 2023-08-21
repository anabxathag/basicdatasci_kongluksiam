import numpy as np

# reshape เปลี่ยนชั่วคราว
a = np.arange(10)
print(a)
print(a.shape)
print(a.reshape((2,5)))
print(a.reshape((2,5)).shape)
print(a)
print()

b = a.reshape((2,5))
print(b)
print(b.shape)
print()

# reshape เปลี่ยนถาวร
b = np.arange(10,20)
print(b)
print(b.shape)
b.resize(5,2)
print(b)
print(b.shape)
