import numpy as np
arr=np.array([[1,2,3],[4,5,6],[7,8,9]])
print(arr)
print(np.ones_like(arr))
print(np.full((2,2),99))
print(np.full_like(arr,4))
print(np.repeat(arr,3,axis=0))
print(np.repeat(arr,3,axis=1))
print(np.repeat(arr,3))