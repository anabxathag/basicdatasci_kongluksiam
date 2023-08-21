import numpy as np

# Access 1-D Arrays
abc = np.array([1,2,3,4,5])
print(abc.shape)    #(col, )
print(abc[1])
print(abc[-2])
print(abc[2]+abc[-1])

# Access 2-D Arrays
abc = np.array([[1,2],[3,4],[5,6]])
print(abc.shape)    # (row, col)
print(abc[2])       # abc[row]
print(abc[0][1])    # abc[row][col]
print(abc[-1][0]+abc[2][-1])    # [2][0] + [2][1] = 5 + 6

# Access 3-D Arrays
abc = np.array([[[1,2],[3,4],[5,6]],[[7,8],[9,10],[11,12]]])
print(abc.shape)    # (dept, row, col)
print(abc[0])   # abc[dept]
print(abc[0,1])   # abc[dept][row]
print(abc[0,2,1])   # abc[dept][row][col]
print(abc[0,2,1]+abc[1,0,1])    # 6 + 8
