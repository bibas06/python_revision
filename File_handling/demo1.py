f=open("q1.txt","r")#here instead of r we can write rt but...
data=f.read(10)#it will read only 10 characters
#text mode is by default mode therefore no need to specify t
print(data)#read is default mode
print(type(data))
f.close()
