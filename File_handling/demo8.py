f=open("sample3.txt","a+")
f.write("123")
print(f.read())
f.write("abc")#it gets appended at the end
f.close()
