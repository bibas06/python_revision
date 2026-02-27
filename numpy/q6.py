import numpy as np
arr1=np.array([[1,2,3],[4,5,6],[7,8,9]])
arr2=np.array([[1.0,2.0,3.0]])
print(arr1)
print(arr1.dtype)#1 byte=8 bits for integer size=4 bytes
print(arr1.itemsize)#give result in bytes
print(arr2.ndim)
print(arr2.itemsize)#for float size=8 bytes
print(arr2.dtype)#give result in <data type>bits
print(arr1.size*arr1.itemsize)#get total size