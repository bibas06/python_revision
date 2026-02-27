import sys
try:
    f=open("sample1.txt","r")
    f.write("hello fuckers")
except Exception as obj:
    print(obj)
    print(sys.exc_info()[0])
    print(sys.exc_info()[1])
else:
    f.close()
finally:
    print("rest of the code")