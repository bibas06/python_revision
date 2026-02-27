f=open("q1.txt","a")
f.write("i am here to fuck u guys")
f.close()
'''r,r+,w,w+=Pointer is at the beginning
a=pointer is at the end and cannot be moved for reading
a+=pointer is at the end and can be moved using seek() to raed content
seek(0) pointer moves to the beginning
w,w+,a,a+=creates file if does not exists
but w,w+ overwrites
'''
