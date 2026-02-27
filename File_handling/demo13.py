word="learning"
line_no=1
with open("sample5.txt","r") as f:
    while True:
        data=f.readline()
        if(word in data):
            print("found at line number :",line_no)
            break
        else:
            line_no+=1