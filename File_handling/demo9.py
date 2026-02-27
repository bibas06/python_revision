with open("sample4.txt","r+") as f:
    print(f.read())
    #here no need to close the file
with open("sample4.txt","w") as f:
    f.write("asshole")
    