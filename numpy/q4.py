import numpy as np
l1=[1,2,3,4,5]
l2=[[1,2,3,4,5],[2,3,4,7,8],[4,5,6,7,8]]
arr1=np.array(l1)
arr2=np.array(l2)
print(arr2)
print(arr2[1:,2:])
a1=np.arange(0,10,step=2)
print(a1)
a2=np.linspace(1,10,100)
print(a2)
#imp: like list u can also use copy() in an array
#an array is also a reference data type