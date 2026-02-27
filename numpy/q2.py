import numpy as np
my_list1=[1,2,3,4,5]
my_list2=[6,7,8,9,10]
my_list3=[2,5,6,4,9]
arr=np.array([my_list1,my_list2,my_list3])
print(arr)
print(arr[0][4])
print(arr[0,4])
print(arr.shape)#it will display rows and columns in tuple format
                 #(3,5)
print(arr.reshape(5,3))