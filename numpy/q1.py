import numpy as np
my_lst=[1,2,3,4]
arr=np.array(my_lst)
print(arr.ndim)#to get dimension
print(type(arr))
print(arr[3])
print(arr)
print(arr.shape)#an in-built function which specifies how many no. rows and
                #columns are there
                #(4,) for 1-D array
#NumPy is faster than lists because of its fixed type and it consumes 
#less memory space
#Faster to read less bytes of memory
#no type checking when iterating through objects
#NumPy uses contiguous memory