word="learning"
with open("sample5.txt","r") as f:
    data=f.read()
    print(data)
    if(data.find(word)!=-1):
        print("found")
    else:
        print("Not found")    
