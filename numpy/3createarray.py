import numpy as np

# Create 0-D Arrays
aba = np.array(43)
print(aba)
print(aba.ndim)     # Number of Dimensions

# Create 1-D Arrays
bcb = np.array([1,2,3,4])   # List
cdc = np.array((1,2,3,4))   # Tupple
print(bcb)
print(bcb.ndim)
print(cdc)
print(cdc.ndim)

# Create 2-D Arrays
aba = np.array(([1,2,3],[4,5,6]))
print(aba)
print(aba.ndim)
bcb = np.array([[1,2,3],(4,5,6)])
print(bcb)
print(bcb.ndim)
cdc = np.array([(1,2,3),(4,5,6)])
print(cdc)
print(cdc.ndim)

# Create 3-D Arrays
aba = np.array([[[2,4,8,16],(3,9,27,81)],((4,16,64,256),[5,25,125,625])])
print(aba)
print(aba.ndim)
