import numpy as np

abc = np.array([1,2,3,4,5])
print(abc)
print(abc.dtype)

abc = np.array([1,2,3,4,5], dtype='int')
print(abc)
print(abc.dtype)

abc = np.array([1,2,3,4,5], dtype='float')
print(abc)
print(abc.dtype)

abc = np.array([[1,2,3,4,5],[6,7,8,9,10]], dtype='complex')
print(abc)
print(abc.dtype)

abc = np.array([False,True,True,False,True,False])  # boolean
print(abc)
print(abc.dtype)

abc = np.array(["1","arto","False"])    # Strings
print(abc)
print(abc.dtype)
