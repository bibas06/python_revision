"""def  even(num):
    if num%2==0:
        return True"""
lst=[0,1,2,3,4,5,6,7,8,9,10]
#print(list(filter(even,lst)))
#print(list(map(even,lst)))
print(list(filter(lambda num:num%2==0,lst)))
print(list(map(lambda num:num%2==0,lst)))
print(list(map(lambda num:num+2,lst)))
print(list(filter(None,lst)))#returns all True value i.e all non zero elements
#bool(non zero value)=True    when function is none
#bool(None)=False