num=5
while num>0:
    if num==3:
        break
    else:
        print(num)
        num=num-1
num=0
while num<5:
    num=num+1
    if num==3:
        continue
    else:
        print(num)