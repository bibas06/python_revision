def display(name,age):
    print(f"{name} has age {age} ")
display(name='jay',age=20)#keyword arguments
display("bibas",20)#positional arguments
display("nikhil",age=29)#mixing positional and keyword agruments
display(age=25,name="ansh")
#display(age=22,"suvam")
#error is diplayed since
#Positional argument cannot appear after keyword arguments
def data(name,age,sex='male'):#default agument should present at last in func. defination
    print(f"{name} is a {sex} and has age {age}")
data("manish",age=19)
data("yoshita",20,sex='female')