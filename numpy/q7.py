import numpy as np
arr=np.array([[1,2,3,4,5],[6,7,4,5,6],[8,9,7,8,9]],ndmin=2)
print(arr)
print(arr[0,:])
print(arr[0,0:5:2])#arr[row,startindex:stopindex:stepindex]
print(arr[0:,2:])
