with open("sample6.txt","r") as f:
    data=f.read()
    print(data)
nums=data.split(",")#converts string to list    
print(nums)
count=0
l=len(nums)
for i in range(l):
    if(int(nums[i])%2==0):
        count+=1
    else:
        continue
print(count)    