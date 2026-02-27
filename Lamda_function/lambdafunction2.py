data=(["bibas samal",'ansh somaiya','manish jeet','aman kumar','suvam dhar','snehashis sha'])
print(sorted(data))
print(sorted(data,key=len))
print(sorted(data,key=lambda x:x.split()[1]))