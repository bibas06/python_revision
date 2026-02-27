#we can pass a function object as an argument to other function
def get_name():
    nm=input("enter your first name")
    lm=input("enter your last name")
    return nm+''+lm
def display1(func):#1 higher order function
    print(func())
    print(func)
def display2(func):#2
    print(func)
display1(get_name)#function object is get_name
display2(get_name())
#use either 1 or 2