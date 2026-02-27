#unpacking of tuples
tup=(1,2,3,4,5)
l=list(tup)
i1,*i2,i3=tup
print(i1)
print(i3)
print(i2)#store elements in list format
import sys
print(sys.getsizeof(tup),"bytes")
print(sys.getsizeof(l),"bytes")