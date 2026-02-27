a={}         #sets are mutable but each elemnts in a set are immutable
print(type(a))  #u can add and remove element                
b=set()
print(type(b))
c=(1,)
d=(2)
print(type(c))
print(type(d))
s={1,2,4,6,8,9,4,2}
s.add(199)
#s.add([1,2,3])
print(s)
s.pop()
print(s) 