f=open("sample2.txt","w+")
print(f.read())#in this mode the file opened in truncated mode i.e. all data will get wiped out
f.write("abc")
print(f.read())
f.close()