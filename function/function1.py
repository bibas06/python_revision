#scope of local variables/identifiers
def display(name):#here name and age are local variables
    age=20
    print(f"{name} has age {age}")
    print(locals())
    print(len(locals()))
    def inner():#it is a local identifier
        pass
display("bibas")    